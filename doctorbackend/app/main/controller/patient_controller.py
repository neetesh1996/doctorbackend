from flask import request, redirect
from flask_restplus import Resource
from ..util.dto import PatientDto
from ..service.patient_service import post_patient_details, get_patient_details, put_patient_details

import os

api = PatientDto.api
_user = PatientDto.address


@api.route('/')
class UserList(Resource):
    @api.doc('list_of_patient_details')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all patient_details"""
        patient_id = request.args['patient_id']
        auth_header = request.headers.get('Authorization')
        return get_patient_details(auth_header, patient_id)

    @api.response(201, 'Patient successfully created.')
    @api.doc('create a new Patient')
    # @api.expect(_user, validate=True)
    def post(self):
        """Creates a new Patient """
        if 'file' not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files['file']

        data = request.form
        print(data)
        auth_header = request.headers.get('Authorization')
        return post_patient_details(auth_header, data, file)

    @api.response(201, 'Patient successfully updated.')
    @api.doc('updated Patient')
    @api.expect(_user, validate=True)
    def put(self):
        """updated  Patient """
        patient_id = request.args['patient_id']
        data = request.json
        auth_header = request.headers.get('Authorization')
        return put_patient_details(auth_header, data, patient_id)
