from flask import request
from flask_restx import Resource

from ..util.dto import EmailDto
from ..service.email_service import save_new_email, get_all_emails, get_an_email
from typing import Dict, Tuple

api = EmailDto.api
_email = EmailDto.email


@api.route('/')
class EmailList(Resource):
    @api.doc('list_of_registered_emails')
    @api.marshal_list_with(_email, envelope='data')
    def get(self):
        """List all registered emails"""
        return get_all_emails()

    @api.expect(_email, validate=True)
    @api.response(201, 'Email successfully created.')
    @api.doc('create a new email')
    def post(self) -> Tuple[Dict[str, str], int]:
        """Creates a new Email """
        data = request.json
        return save_new_email(data=data)


@api.route('/<event_id>')
@api.param('event_id', 'The Email identifier')
@api.response(404, 'Email not found.')
class Email(Resource):
    @api.doc('get a email')
    @api.marshal_with(_email)
    def get(self, event_id):
        """get a email given its identifier"""
        email = get_an_email(event_id)
        if not email:
            api.abort(404)
        else:
            return email



