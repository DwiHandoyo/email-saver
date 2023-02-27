from flask_restx import Namespace, fields


class EmailDto:
    api = Namespace('email', description='email related operations')
    email = api.model('email', {
        'email_subject': fields.String(required=True, description='email subject'),
        'email_content': fields.String(required=True, description='email content'),
    })


