from flask_restplus import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        # 'username': fields.String(required=True, description='user username'),
        'firstname': fields.String(required=True, description='user firstname'),
        'lastname': fields.String(required=True, description='user lastname'),
        'phone': fields.String(required=True, description='user phone'),
        # 'password': fields.String(required=True, description='user password'),
        # 'public_id': fields.String(description='user Identifier')
        'id': fields.Integer(required=False, description='user id'),
    })

class AuthDto:
    api = Namespace('user', description='authentication related operations')
    user_auth = api.model('user', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })  
class AddressDto:
     api = Namespace('address', description='user related operations')
     address = api.model('address', {
        'address1': fields.String(required=True, description='address address1 address'),
        # 'addressname': fields.String(required=True, description='address addressname'),
        'city': fields.String(required=True, description='address city'),
        'state': fields.String(required=True, description='address state'),
        'country': fields.String(required=True, description='address country'),
        'followup': fields.String(required=True, description='address followup'),
        'department': fields.String(description='address department'),
        'address_id': fields.Integer(required=False, description='address address_id'),
        
    })

class PatientDto:
     api = Namespace('patient', description='user related operations')
     address = api.model('patient', {
         'image_url': fields.String(required=False, description='patient_details image_url '),
        'patient_name': fields.String(required=False, description='patient_details patient_name '),
        'primary_complaints': fields.String(required=False, description='patient_details primary_complaints'),
        'description': fields.String(required=False, description='patient_details description'),
        'duration': fields.String(required=False, description='patient_details duration'),
        'payment': fields.String(required=False, description='patient_details payment'),
        'patient_id': fields.Integer(required=False, description='patient_details patient_id'),
        # 'department': fields.String(description='patient_details department')
    })

class ScheduleDto:
     api = Namespace('schedule', description='user related operations')
     address = api.model('schedule', {
        'image_url': fields.String(required=False, description='schedule image_url '),
        'patient_name': fields.String(required=False, description='schedule patient_name '),
        'complaints': fields.String(required=False, description='schedule complaints'),
        'language': fields.String(required=False, description='schedule language'),
        'gender': fields.String(required=False, description='schedule gender'),
        'date': fields.String(required=False, description='schedule date'),
        'time': fields.String(required=False, description='schedule time'),
        'schedule_id': fields.Integer(required=False, description='history Schedule_id'),
        # 'department': fields.String(description='patient_details department')
    })   

class HistoryDto:
     api = Namespace('history', description='user related operations')
     address = api.model('history', {
        'image_url': fields.String(required=False, description='history image_url '),
        'patient_name': fields.String(required=False, description='history patient_name '),
        # 'complaints': fields.String(required=False, description='history complaints'),
        # 'language': fields.String(required=False, description='history language'),
        'date': fields.String(required=False, description='history date'),
        'time': fields.String(required=False, description='history time'),
        'schedule_id': fields.Integer(required=False, description='history Schedule_id'),
        # 'department': fields.String(description='patient_details department')
    })    

