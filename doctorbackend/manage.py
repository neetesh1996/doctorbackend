
import os
# import unittest
from app.main.model import user
from app.main.model import address
from app.main.model import patient
from app.main.model import schedule
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from app import blueprint
from app.main import create_app, db
# from app.main.model import blacklist

user = db.relationship("User", back_populates="address", cascade="all, delete-orphan")
address = db.relationship('Address', back_populates='user', lazy=True, cascade="all, delete-orphan")

user = db.relationship("User", back_populates="patient", cascade="all, delete-orphan")
patient = db.relationship('Patient', back_populates='user', lazy=True, cascade="all, delete-orphan")

patient = db.relationship("Patient", back_populates="schedule", cascade="all, delete-orphan")
schedule = db.relationship('Schedule', back_populates='patient', lazy=True, cascade="all, delete-orphan")

user = db.relationship("User", back_populates="schedule", cascade="all, delete-orphan")
schedule = db.relationship('Schedule', back_populates='user', lazy=True, cascade="all, delete-orphan")

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()

manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)

@manager.command
def run():
    app.run()

# @manager.command
# def test():
#     """Runs the unit tests."""
#     tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
#     result = unittest.TextTestRunner(verbosity=2).run(tests)
#     if result.wasSuccessful():
#         return 0
#     return 1

if __name__ == '__main__':
    manager.run()