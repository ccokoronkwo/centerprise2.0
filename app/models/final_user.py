from role import Role

class FinalUser(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    social_id = db.Column(db.String(64), nullable=True, unique=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(255))
    create_date = db.Column(db.DateTime, default=datetime.datetime.now)
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(db.String(45))
    current_login_ip = db.Column(db.String(45))
    login_count = db.Column(db.Integer)
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))