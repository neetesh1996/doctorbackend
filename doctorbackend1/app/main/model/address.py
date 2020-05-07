from .. import db, flask_bcrypt
import datetime

from app.main.model.user import User

from ..config import key

class Address(db.Model):
    """ Address Model for storing Address related details """
    __tablename__ = "address"

    address_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address1 = db.Column(db.String(50), unique=False)
    city = db.Column(db.String(50), unique=False)
    state = db.Column(db.String(50), unique=False)
    country= db.Column(db.String(50), unique=False)
    followup = db.Column(db.String(255), unique=False)
    department= db.Column(db.String(100))
    # user = db.relationship("User", back_populates="address")
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __repr__(self):
        return "<Address '{}'>".format(self.city)
       