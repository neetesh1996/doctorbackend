import uuid
import datetime

from app.main import db
from app.main.model.user import User
import jwt
from ..config import key

def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        new_user = User(
            # public_id=str(uuid.uuid4()),
            email=data['email'],
            firstname=data['firstname'],
            lastname=data['lastname'],
            phone=data['phone'],
            password=data['password']
            # registered_on=datetime.datetime.utcnow()
            
        )
        save_changes(new_user)
        response_object = {
            'status': 'success',
            'message': 'Successfully registered.'
        }
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
        return response_object, 409

def put_user(token,data,user_id):
        if token:
            auth_token=token.split(" ")[1]
        if not data:
               return {'message': 'No input data provided'}, 400
        if auth_token:
            resp= jwt.decode(auth_token,key)
            print(resp)
            user = User.query.filter_by(id=user_id).first()
            if not user:
               return {'message': 'user does not exist'}, 404
            if not isinstance(resp, str):
               
                user.email=data['email'],
                user.firstname=data['firstname'],
                user.lastname=data['lastname'],
                user.phone=data['phone'],
                user.password=data['password']
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



# def get_all_users():
#     return User.query.all()


# def get_a_user(id):
#     return User.query.filter_by(id=id).first()


def save_changes(data):
    db.session.add(data)
    db.session.commit()


class Auth:

    @staticmethod
    def login_user(data):
        try:
            # fetch the user data
            user = User.query.filter_by(email=data.get('email')).first()
            if user and user.check_password(data.get('password')):
                auth_token = user.encode_auth_token(user.id)
                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'Authorization': auth_token.decode()
                    }
                    return response_object, 200
            else:
                response_object = {
                    'status': 'fail',
                    'message': 'email or password does not match.'
                }
                return response_object, 401

        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Try again'
            }
            return response_object, 500
    
    @staticmethod
    def get_all_users(data):
        # auth_token = new_request.headers.get('Authorization')
        if data:
            auth_token = data.split(" ")[1]
        else:
            return('Provide a valid auth token.')
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            print(resp)
            if not isinstance(resp, str):
                # get all user
                return User.query.all()
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

    @staticmethod
    def get_a_user(args,data):
        # auth_token = new_request.headers.get('Authorization')
        if data:
            auth_token = data.split(" ")[1]
            
        else:
            return('Provide a valid auth token.')
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            print(resp,args)
            
            if not isinstance(resp, str):
                # get all user
                return User.query.filter_by(id=args).first()
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