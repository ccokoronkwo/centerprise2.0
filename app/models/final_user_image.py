from final_user import FinalUserImage

class FinalUserImage(BaseModel):
    user_id =  db.Column(db.Integer, db.ForeignKey('final_user.id'))
    image_filename = db.Column(db.String, default=None, nullable=True)
    image_url = db.Column(db.String, default=None, nullable=True)