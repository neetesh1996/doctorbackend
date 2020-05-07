from flask import request, jsonify
from flask_restplus import Resource
from app.main.service.user_service import Auth
from ..util.dto import UserDto, AuthDto
from ..service.user_service import save_new_user, put_user
# from app.main.model.user import User

api = UserDto.api
_user = UserDto.user
user_auth = AuthDto.user_auth


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_users')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered users"""
        auth_header = request.headers.get('Authorization')
        return Auth.get_all_users(data=auth_header)

    @api.response(201, 'User successfully created.')
    @api.doc('create a new user')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new User """
        data = request.json
        return save_new_user(data=data)
    
    @api.response(201, 'Patient successfully updated.')
    @api.doc('updated Patient')
    @api.expect(_user, validate=True)
    def put(self):
        """updated  Patient """
        user_id= request.args['user_id']
        data = request.json
        auth_header = request.headers.get('Authorization')
        return put_user(auth_header,data,user_id)
     


@api.route('/byid')
@api.param('id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('get a user')
    @api.marshal_with(_user)
    def get(self):
        """get a user given its identifier"""
        id= request.args['id'] #params
        print(id)
        auth_header = request.headers.get('Authorization')
        user = Auth.get_a_user(id,auth_header)
        # return id
        if not user:
            api.abort(404)
        else:
            return user


@api.route('/login')
class UserLogin(Resource):
    """
        User Login Resource
    """
    @api.doc('user login')
    @api.expect(user_auth, validate=True)
    def post(self):
        #  post data
        post_data = request.json
        return Auth.login_user(data=post_data)

