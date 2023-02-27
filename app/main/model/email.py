
from .. import db


class Email(db.Model):
    """ Email Model for storing email related details """
    __tablename__ = "email"

    event_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email_subject = db.Column(db.String(), unique=True, nullable=False)
    email_content = db.Column(db.String(), unique=True, nullable=False)
    time_stamp = db.Column(db.String(20), unique=True, nullable=False)

    def __repr__(self):
        return "<Email '{}'>".format(self.email_subject)
