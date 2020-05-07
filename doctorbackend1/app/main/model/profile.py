from .. import db, flask_bcrypt
import datetime

from app.main.model.user import User

from ..config import key



class Profile(db.Model):
    """Profile Model for storing Profile related details """
    __tablename__ = "profile"

    profile_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    basic= db.Column(db.String(250), unique=False)
    address = db.Column(db.String(50), unique=False)
    education = db.Column(db.String(50), unique=False)
    certification = db.Column(db.String(50), unique=False)
    professional = db.Column(db.String(50), unique=False)
    experience= db.Column(db.String(255), unique=False)
    availability = db.Column(db.String(100),unique=False)
    # user = db.relationship("User", back_populates="address")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __repr__(self):
        return "<Profile '{}'>".format(self.profile_id)
       