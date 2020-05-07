from app.main import db
from app.main.model.address import Address
import jwt
from ..config import key




def post_address(token,data):
        if token:
            auth_token=token.split(" ")[1]
        else:
            return ('Please provide valid token')
        try:

            if auth_token:
                
                resp= jwt.decode(auth_token,key)
                print(resp)
                if not isinstance(resp, str):
                    new_address= Address(
                    address1 =data['address1'],
                    city=data['city'],
                    state=data['state'],
                    country=data['country'],
                    followup=data['followup'],
                    department=data['department'],
                    user_id=resp['sub'] #on hold
                    )
                    save_changes(new_address)
                
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
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'            

def put_address(token,data,address_id):
        if token:
            auth_token=token.split(" ")[1]
        if not data:
               return {'message': 'No input data provided'}, 400
    
        if auth_token:
            resp= jwt.decode(auth_token,key)
            print(resp)
            address = Address.query.filter_by(address_id=address_id).first()
            print(address)
            if not address:
               return {'message': 'Address does not exist'}, 400
            if not isinstance(resp, str):
               
                # patient.patient_name =data['patient_name'],
                address.address1 =data['address1'],
                address.city=data['city'],
                address.state=data['state'],
                address.country=data['country'],
                address.followup=data['followup'],
                address.department=data['department'],
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
    
def get_address(token):
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
                return Address.query.filter_by(user_id=resp['sub']).first() #on hold
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







    # @staticmethod
def save_changes(data):
       db.session.add(data)
       db.session.commit()           




