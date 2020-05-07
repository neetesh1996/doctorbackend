from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.address_controller import api as add_ns
from .main.controller.patient_controller import api as pat_ns
from .main.controller.schedule_controller import api as sch_ns

blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(blueprint,
          title='Doctor',
          version='1.0',
          description='doctor backend'
          )

api.add_namespace(user_ns )#path='/api'
api.add_namespace(add_ns)
api.add_namespace(pat_ns)
api.add_namespace(sch_ns)