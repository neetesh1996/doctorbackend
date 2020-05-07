from app.main import db
from flask import Flask, send_file
from app.main.model.patient import Patient
from app.main.model.user import User
# from  app.main import app
import os
from io import BytesIO
import jwt
from ..config import key

from werkzeug.utils import secure_filename

PROJECT_HOME = os.path.dirname(os.path.realpath(__file__))
UPLOAD_FOLDER = '{}\\uploads\\'.format(PROJECT_HOME)
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


ALLOWED_EXTENSIONS = set([ 'png', 'jpg', 'jpeg', 'gif'])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS




def post_patient_details(token,data,file):
        if token:
            auth_token=token.split(" ")[1]
        else:
            return ('Please provide valid token')
          
        if auth_token:
            resp= jwt.decode(auth_token,key)
            print(resp,data,file)
            # user = User.query.filter_by(id=resp['sub']).first()
            # print(user)
            if file and allowed_file(file.filename):
		             filename = secure_filename(file.filename)
		             file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            print(file,file.filename,file.read())
            if not isinstance(resp, str):
                
                new_patient= Patient(
                image_url = os.path.join(app.config['UPLOAD_FOLDER']+filename),   
                # patient_name =user.firstname +' '+ user.lastname,
                patient_name=data['patient_name'],
                primary_complaints=data['primary_complaints'],
                description=data['description'],
                duration=data['duration'],
                payment=data['payment'],
                # department=data['department'],
                user_id=resp['sub']
            )
            save_changes(new_patient)
            
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

    
def get_patient_details(token,patient_id):
        # auth_token = new_request.headers.get('Authorization')
        if token:
            auth_token = token.split(" ")[1]
        else:
            return('Provide a valid auth token.')
        if auth_token:
            resp = jwt.decode(auth_token,key)
            print(resp)
            # patient=Patient.query.filter_by(patient_id=4).first()
            # print(patient)
            # print( send_file(BytesIO(patient.image_url)))
            if not isinstance(resp, str):
                # get address
                return Patient.query.filter_by(patient_id=patient_id).first()
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

def put_patient_details(token,data,patient_id):
        if token:
            auth_token=token.split(" ")[1]
        if not data:
               return {'message': 'No input data provided'}, 400
        if auth_token:
            resp= jwt.decode(auth_token,key)
            print(resp)
            patient = Patient.query.filter_by(patient_id=patient_id).first()
            if not patient:
               return {'message': 'Patient does not exist'}, 404
            if not isinstance(resp, str):
               
                patient.patient_name =data['patient_name'],
                patient.primary_complaints=data['primary_complaints'],
                patient.description=data['description'],
                patient.duration=data['duration'],
                patient.payment=data['payment'],
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






    # @staticmethod
def save_changes(data):
       db.session.add(data)
       db.session.commit()           




