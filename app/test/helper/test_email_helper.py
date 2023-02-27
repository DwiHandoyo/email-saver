from app.main.model.email import Email
from app.main import db
from sqlalchemy import text

def verify_available_subject(subject):
    sql = text("SELECT * from email WHERE email_subject = '{subject}'".format(subject=subject))
    results = db.engine.execute(sql)
    return results.mappings().all()

    