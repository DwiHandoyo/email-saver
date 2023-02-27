from flask_restx import Api
from flask import Blueprint

from .main.controller.email_controller import api as email_ns

blueprint = Blueprint('api', __name__)
authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    }
}


api = Api(
    blueprint,
    title='Email Saver',
    version='1.0',
    description='an email saver',
    authorizations=authorizations,
    security='apikey'
)

api.add_namespace(email_ns, path='/save_email')
