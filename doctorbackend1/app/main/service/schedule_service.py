from app.main import db
from flask import Flask
from app.main.model.schedule import Schedule
# from app.main.model.user import User
from app.main.model.patient import Patient


# from  app.main import app
import os
import jwt
from ..config import key

# from werkzeug.utils import secure_filename

# PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
# UPLOAD_FOLDER = '{}\\uploads\\'.format(PROJECT_HOME)
# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


# ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg', 'gif'])

# def allowed_file(filename):
# 	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




def post_schedule(token,data,patient_id):
        if token:
            auth_token=token.split(" ")[1]
        else:
            return ('Please provide valid token')
          
        if auth_token:
            resp= jwt.decode(auth_token,key)
            print(resp)
            patient = Patient.query.filter_by(patient_id=patient_id).first()
            if not patient:
                response = {
                    'status': 'fail',
                    'message': 'No such Patient exist'
                }
                return response, 400
               
            if not isinstance(resp, str):
                
                new_schedule= Schedule(
                image_url = patient.image_url,    
                # patient_name =user.firstname +' '+ user.lastname,
                patient_name = patient.patient_name,
                complaints=data['complaints'],
                language=data['language'],
                gender=data['gender'],
                date=data['date'],
                time=data['time'],
                # department=data['department'],
                patient_id=patient.patient_id,
                user_id=resp['sub']
            )
            save_changes(new_schedule)
            
            response_object = {
                'status': 'success',
                'message': 'Successfully created.'
            }
            return response_object, 201
            
        else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401 

    
def get_schedule(token):
        # auth_token = new_request.headers.get('Authorization')
        if token:
            auth_token = token.split(" ")[1]
        else:
            return('Provide a valid auth token.')
        if auth_token:
            resp = jwt.decode(auth_token,key)
            
            print(resp)
            if not isinstance(resp, str):
                # get address
                # return Schedule.query.filter_by(user_id=resp['sub']).first()
                return Schedule.query.all()
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 403            

def put_schedule(token,data,schedule_id):
        if token:
            auth_token=token.split(" ")[1]
        if not data:
               return {'message': 'No input data provided'}, 400
        try:
            if auth_token:
                resp= jwt.decode(auth_token,key)
                print(resp)
                schedule = Schedule.query.filter_by(schedule_id=schedule_id).first()
                print(schedule)
                if not schedule:
                   return {'message': 'Patient does not exist'}, 400
                if not isinstance(resp, str):
                    # patient.patient_name =data['patient_name'],
                    schedule.complaints=data['complaints'],
                    schedule.language=data['language'],
                    schedule.gender=data['gender'],
                    schedule.date=data['date'],
                    schedule.time=data['time'],
                    # department=data['department'],
                    # patient.user_id=resp['sub']
                    db.session.commit()
                response_object = {
                    'status': 'success',
                    'message': 'Successfully updated.'
                }
                return response_object, 201
            else:
                response_object = {
                    'status': 'fail',
                    'message': resp
                }
                return response_object, 401 
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'  


def get_history(token,data):
        # auth_token = new_request.headers.get('Authorization')
        if token:
            auth_token = token.split(" ")[1]
        else:
            return('Provide a valid auth token.')
        try:    
            if auth_token:
                resp = jwt.decode(auth_token,key)
                print(resp)
                if not isinstance(resp, str):
                    patients = Schedule.query.filter(Schedule.date.between(data['fromDate'], data['toDate'])).all()
                    if not patients:
                        return {'message': 'Patient does not exist this range'}, 404
                    else:
                        return patients
                else:
                    response_object = {
                        'status': 'fail',
                        'message': resp
                    }
                    return response_object, 401
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'Provide a valid auth token.'
                }
                return response_object, 403        
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.',401
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.',403




    # @staticmethod
def save_changes(data):
       db.session.add(data)
       db.session.commit()           




