from datetime import datetime, timezone, timedelta

from app.main import db
from app.main.model.email import Email
from typing import Dict, Tuple

def save_new_email(data: Dict[str, str]) -> Tuple[Dict[str, str], int]:
    
    new_email = Email(
        email_subject=data['email_subject'],
        email_content=data['email_content'],
        time_stamp=f'{datetime.now(timezone(timedelta(hours=+8))):%Y-%m-%d %H:%M}'
    )
    save_changes(new_email)
    response_object = {
        'status': 'succes',
        'message': 'email saved'
    }
    return response_object, 200


def get_all_emails():
    return Email.query.all()


def get_an_email(event_id):
    return Email.query.filter_by(event_id=event_id).first()

def save_changes(data: Email) -> None:
    db.session.add(data)
    db.session.commit()

