from .. import db, flask_bcrypt
import datetime

from app.main.model.user import User

from ..config import key



class Patient(db.Model):
    """ Patient Model for storing patient related details """
    __tablename__ = "patient_details"

    patient_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image_url= db.Column(db.String(250), unique=False)
    patient_name = db.Column(db.String(50), unique=False)
    primary_complaints = db.Column(db.String(50), unique=False)
    description = db.Column(db.String(50), unique=False)
    duration = db.Column(db.String(50), unique=False)
    payment = db.Column(db.String(255), unique=False)
    # department= db.Column(db.String(100))
    # user = db.relationship("User", back_populates="address")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __repr__(self):
        return "<Patient '{}'>".format(self.patient_id)
       