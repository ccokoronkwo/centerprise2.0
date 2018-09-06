from base import BaseModel
from base import db

class Invoice(db.Model, CrudModel):
    id = db.Column(db.Integer, primary_key=True)
    vendor_id = db.Column(db.Integer, db.ForeignKey('vendor.id'))
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'))
    payroll_period_id = db.Column(db.Integer, db.ForeignKey('payroll_period.id'))
    department = db.relationship('Department', backref='invoices')
    payroll_period = db.relationship('PayrollPeriod', backref="invoices")
    subdepartment = db.Column(db.Text, default='')
    vendor = db.relationship('Vendor', lazy="joined", backref=db.backref('invoices', lazy="dynamic"))
    recurring = db.Column(db.Boolean)
    recurring_without_amounts = db.Column(db.Boolean)
    number = db.Column(db.Text)
    date = db.Column(db.Date)
    date_posted = db.Column(db.Date)
    amount = db.Column(db.Numeric(asdecimal=True, scale=2))
    memo = db.Column(db.Text)
    upload = db.Column(db.Text)
    allocation = db.Column(db.Text)

    other_entity_allocation = db.Column(db.Text)

    groups = db.Column(postgresql.ARRAY(db.Text))
    subgroups = db.Column(postgresql.ARRAY(db.Text))

    facility_amounts = db.relationship('InvoiceFacilityAmount', cascade="all, delete-orphan")
    original_invoice_id = db.Column(db.Integer, db.ForeignKey('invoice.id')) # for voids, adjusts

    flag = db.Column(db.Text, default='') # void,adjust, monthly-invoice
    type = db.Column(db.Text, default='invoice') # invoice/payroll/ach

    completed = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.Date, default=datetime.today())
    imported = db.Column(db.Boolean, default=False)
    pass_through = db.Column(db.Boolean, default=False)

    def get_label(self, field, default_label):
        if field == 'pass_through':
            return ''
        else:
            return super(Invoice, self).get_label(field, default_label)

    def get_pretty(self, field, for_html=False):
        if field == 'pass_through':
            return render_template_string('''
                <input type="checkbox" class="invoice-pass-through-checkbox" data-url="{{url_for('toggle_pass_through', invoice_id=invoice.id)}}" {% if invoice.pass_through %}checked="checked" {% endif %}/>
            ''', invoice=self)
        else:
            return super(Invoice, self).get_pretty(field, for_html=for_html)

    def pretty_gls(self):
        return ', '.join(str(gl)  for a in self.allocations for gl in a.general_ledger_details)

    def pretty_groups(self):
        return ', '.join(str(group) for a in self.allocations for group in a.groups)

    def pretty_allocations(self):
        return ', '.join(str(a.allocation) for a in self.allocations)

    def css_classes(self):
        if self.completed != True:
            return 'invoice-not-completed'
        return ''

    def pretty_vendor(self):
        if self.type == 'payroll':
            return "%s" % self.department
        return "%s" % self.vendor

    def after_commit(self):
        if not self.type == 'ach':
            CachedAllocation.update_invoice(self)

    def before_delete(self):
        CachedAllocation.query.filter_by(invoice_id=self.id).delete()

        if self.flag == 'void':
            adjust = Invoice.query.filter_by(original_invoice_id=self.original_invoice_id, flag='adjust').first()
            original_invoice = Invoice.query.filter_by(id=self.original_invoice_id).first()

            if adjust:
                adjust.before_delete()
                flash('Deleted associated adjust: %s deleted' % adjust, 'success') 
                db.session.delete(adjust)
            if original_invoice:
                original_invoice.flag = ''
                flash("Removed 'voided' flag from original invoice: %s." % original_invoice, 'success') 
                db.session.add(original_invoice)
            db.session.commit()



    def can_edit(self):
        return after_current_lock_date(self.date_posted) and self.flag not in ('void', 'voided', 'monthly credit')

    def can_delete(self):
        return after_current_lock_date(self.date_posted) 

    @classmethod
    def generate_flat_fee_monthly_credit_invoice(cls, date):
        ff_total = MonthlyAmount.total_flat_fee_monthly_amount(date.month, date.year)
        sum_portion = util.sum_currency(CachedAllocation.portion)

        first_date = util.first_date_of_month(date.month, date.year)
        last_date = util.last_date_of_month(date.month, date.year)

        exempted_gls = db.session.query(MonthlyCreditExemptedGL.gl_id).subquery()

        gls = (
            db.session.query(CachedAllocation.general_ledger_code_id, 
                            ff_total * over(sum_portion / util.sum_currency(sum_portion)))
                      .outerjoin(Invoice, Invoice.id == CachedAllocation.invoice_id)
                      .filter(CachedAllocation.cfc_group_only==True, 
                              ~CachedAllocation.general_ledger_code_id.in_(exempted_gls),
                              CachedAllocation.date_posted.between(first_date, last_date),
                              db.or_(Invoice.flag != 'monthly credit', Invoice.flag==None))
                      .group_by(CachedAllocation.general_ledger_code_id)
                      .order_by(sum_portion.desc())
         )
        invoice = Invoice(date_posted=date,
                          date=date, 
                          number="%s%s" % (util.month(date.month)[:3], date.year),
                          flag='monthly credit')
        invoice.vendor = Vendor.query.filter_by(name='Monthly Credit').first() or Vendor(name='Monthly Credit')
        invoice.amount = 0
        allocation_1_gls = []
        for gl_id, credit in gls:
            allocation_1_gls.append(AllocationGL(general_ledger_code_id=gl_id, amount=-credit))
            invoice.amount -= credit
        invoice.allocations=[Allocation(groups=['Centers for Care'],
                                        subgroups=[],
                                        allocation='By Bed',
                                        general_ledger_details=allocation_1_gls)]

        if invoice.amount:
            invoice.amount = util.currency_decimal(invoice.amount)
        db.session.add(invoice)
        db.session.commit()
        invoice.after_commit()

        return invoice




    def void(self):
        self.flag = 'voided'

        void_invoice = Invoice(
            vendor_id=self.vendor_id,
            department_id=self.department_id,
            payroll_period_id=self.payroll_period_id,
            subdepartment=self.subdepartment,
            number=self.number + '-V',
            date=self.date,
            date_posted=g.last_open_date,
            amount=-1 * self.amount,
            memo=self.memo,
            upload=self.upload,
            type=self.type,
            original_invoice_id=self.id,
            flag='void',
            completed=True
        )
        void_invoice.allocations = []
        for allocation in self.allocations:
            void_invoice.allocations.append(Allocation(
                display_name=allocation.display_name,
                allocation=allocation.allocation,
                other_entity_allocation=allocation.other_entity_allocation,
                groups=allocation.groups,
                subgroups=allocation.subgroups,
                general_ledger_details=[AllocationGL(general_ledger_code_id=gl.general_ledger_code_id,
                                               amount=-1 * gl.amount)
                                               for gl in allocation.general_ledger_details],
                facility_amounts=[AllocationFacilityAmount(amount=-1 * fa.amount if fa.amount else None,
                                                        facility_id=fa.facility_id) for fa in allocation.facility_amounts]
            ))


        db.session.add(self)
        db.session.add(void_invoice)
        db.session.commit()

        for ca in CachedAllocation.query.filter_by(invoice_id=self.id):
            new_ca = CachedAllocation(
                invoice_id = void_invoice.id,
                facility_id = ca.facility_id,
                general_ledger_code_id = ca.general_ledger_code_id,
                cfc_group_only = ca.cfc_group_only,
                type = ca.type,
                vendor = ca.vendor,
                number = void_invoice.number,
                description = ca.description,
                date = ca.date,
                date_posted = void_invoice.date_posted,
                portion= -1*ca.portion, 
                percent= -1*ca.percent,
                amount = -1 * ca.amount,
                allocation = ca.allocation,
                code =ca.code
            )
            db.session.add(new_ca)
        db.session.commit()
        return void_invoice

        

        
    def facilities_by_group(self, group):
        return (InvoiceFacilityAmount.query
                                     .join(Facility)
                                     .filter(InvoiceFacilityAmount.invoice_id==self.id,
                                             Facility.updates.any(group=group)))



    def applicable_facility_updates(self):
        amounts = db.session.query(InvoiceFacilityAmount.facility_id).filter(InvoiceFacilityAmount.invoice_id == self.id).subquery()
        latest = FacilityUpdate.latest(self.date)
        or_filters = [FacilityUpdate.facility_id.in_(amounts)]
        if self.groups:
            or_filters.append(FacilityUpdate.group.in_(self.groups))
        if self.subgroups:
            or_filters.append(FacilityUpdate.subgroup.in_(self.subgroups))

        latest = latest.filter(db.or_(*or_filters))
        return latest

    def by_entity_entities(self):
        return self.applicable_facility_updates().filter(db.or_(
                db.and_(self.allocation == 'By Entity',
                        FacilityUpdate.group.in_(['Centers for Care', 'Flat Fee', 'Upcoming Facility'])),
                db.and_(self.other_entity_allocation == 'By Entity',
                        FacilityUpdate.group == 'Other Entity'))
        )

    def adjusted_invoice_amount(self):
        latest_other_entities = FacilityUpdate.latest(self.date).filter(FacilityUpdate.group == 'Other Entity').subquery()

        other_entity_sum = (
            db.session.query(util.sum_currency(InvoiceFacilityAmount.amount).label('sum'))
                      .join(latest_other_entities, InvoiceFacilityAmount.facility_id == latest_other_entities.c.facility_id)
                      .filter(InvoiceFacilityAmount.invoice_id == self.id)
                      .first()
        )

        other_entity_sum = other_entity_sum.sum or 0
        if other_entity_sum == 0: 
            return self.amount
        if self.other_entity_allocation == 'By Percent':
            return self.amount - self.amount*other_entity_sum/Decimal(100.0)
        return self.amount - other_entity_sum

    def total_beds(self):
        updates_subq = self.applicable_facility_updates().subquery()
        return db.session.query(db.func.sum(updates_subq.c.beds).label('beds')).first().beds or 0



    @classmethod
    def default_query(cls, type='invoice'):
        locks = db.session.query(PostingPeriodLock.date).subquery()
        return cls.query.filter_by(type=type).join(locks, Invoice.date_posted > locks.c.date)

    @classmethod
    def sum(cls, month, year, type='invoice'):
        return db.session.query(util.sum_currency(Invoice.amount)).filter((Invoice.type == type) & util.filter_by_month_year(Invoice.date_posted, month, year)).scalar() or 0


    
    @classmethod
    def relationship_column_map(cls):
        return {'vendor': {'relationship': cls.vendor, 'column': Vendor.name },
                'department': {'relationship': cls.department, 'column': Department.name},
                'payroll_period': {'relationship': cls.payroll_period, 'column': PayrollPeriod.to_date }}

    @classmethod
    def additional_search_likes(cls, search_query):
        return [Invoice.general_ledger_details.any(GeneralLedgerDetail.general_ledger_code.has(db.or_(GeneralLedgerCode.code.contains(search_query),
                                                                                                      GeneralLedgerCode.description.contains(search_query))))]


    class Meta(CrudModel.Meta):
        display_fields = ('vendor', 'number', 'date', 
                          'date_posted', 'amount', 'flag')
        editable = True
        display_name = 'Invoice'
        order_by = 'date_posted'
        additional_actions = {'print': 'invoice_print',
                              'pdf': 'invoice_pdf'} 

    def __repr__(self):
        return "%s - %s (%s) %s" % (self.pretty_vendor(), self.number, self.amount, self.flag)