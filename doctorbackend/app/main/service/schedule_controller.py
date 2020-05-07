from flask import request, redirect
from flask_restplus import Resource
from ..util.dto import ScheduleDto, HistoryDto
from ..service.schedule_service import post_schedule, get_schedule, put_schedule,get_history

import os

api = ScheduleDto.api
_user = ScheduleDto.address

app=HistoryDto.api
history= HistoryDto.address



@api.route('/')
class UserList(Resource):
    @api.doc('list_of_schedule_details')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """List all schedule_details"""
        auth_header = request.headers.get('Authorization')
        return get_schedule(token=auth_header)

    @api.response(201, 'schedule successfully created.')
    @api.doc('create a new schedule')
    @api.expect(_user, validate=True)
    def post(self):
        """Creates a new schedule """
        # if 'file' not in request.files:
        #         print('No file part')
        #         return redirect(request.url)
        patient_id= request.args['patient_id']
    
        data = request.json 
        auth_header = request.headers.get('Authorization')
        return post_schedule(auth_header,data,patient_id)

    @api.response(201, 'schedule successfully updated.')
    @api.doc('update a  schedule')
    @api.expect(_user, validate=True)
    def put(self):
        """update a  schedule """
        schedule_id= request.args['schedule_id']
        data = request.json
        auth_header = request.headers.get('Authorization')
        return put_schedule(auth_header, data, schedule_id)

@api.route('/history')
class HistoryList(Resource):
    @api.doc('list_of_history_details')
    @api.marshal_list_with(history, envelope='data')
    def post(self):
        """List all history_details"""
        data=request.json
        auth_header = request.headers.get('Authorization')
        return get_history(token=auth_header,data=data)

