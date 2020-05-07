from .. import db, flask_bcrypt
import datetime

# from app.main.model.user import User
# from app.main.model.patient import Patient

from ..config import key



class Schedule(db.Model):
    """ Schedule Model for storing Schedule related details """
    __tablename__ = "schedule"

    schedule_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    image_url= db.Column(db.String(250), unique=False)
    patient_name = db.Column(db.String(50), unique=False)
    complaints = db.Column(db.String(50), unique=False)
    language = db.Column(db.String(50), unique=False)
    gender = db.Column(db.String(50), unique=False)
    date = db.Column(db.DateTime(), unique=False)
    time= db.Column(db.Time(), unique=False)
    # department= db.Column(db.String(100))
    # user = db.relationship("User", back_populates="address")
    patient_id = db.Column(db.Integer, db.ForeignKey('patient_details.patient_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __repr__(self):
        return "<Schedule '{}'>".format(self.schedule_id)
       