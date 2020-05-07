from flask import request
from flask_restplus import Resource
# from app.main.service.address_service import Add
from ..util.dto import AddressDto
from ..service.address_service import post_address, get_address,put_address

api = AddressDto.api
_user = AddressDto.address
# user_auth = addressDto.user_auth


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_registered_address')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all registered address"""
        auth_header = request.headers.get('Authorization')
        return get_address(token=auth_header)

    @api.response(201, 'Address successfully created.')
    @api.doc('create a new address')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new address """
        data = request.json
        auth_header = request.headers.get('Authorization')
        return post_address(token=auth_header,data=data)

    @api.response(201, 'address successfully updated.')
    @api.doc('update a  address')
    @api.expect(_user, validate=True)
    def put(self):
        """update a  address """
        address_id= request.args['address_id']
        data = request.json
        auth_header = request.headers.get('Authorization')
        return put_address(auth_header, data, address_id)    


