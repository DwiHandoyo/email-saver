import unittest

from datetime import datetime, timezone, timedelta
from sqlalchemy import text

from app.main import db
from app.main.service.email_service import save_new_email
from app.main.model.email import Email
from app.test.base import BaseTestCase
from app.test.helper.test_email_helper import verify_available_subject


class TestEmailService(BaseTestCase):

    def test_save_new_email(self):
        data = {
            "email_subject":"test",
            "email_content":"test_content"
        }
        email = Email(
            email_subject=data["email_subject"],
            email_content=data["email_content"],
            time_stamp=f'{datetime.now(timezone(timedelta(hours=+8))):%Y-%m-%d %H:%M}'
        )
        save_new_email(data)

        saved_email = verify_available_subject(data["email_subject"])

        self.assertTrue(len(saved_email)==1)
        self.assertTrue(saved_email[0]["email_content"]==data["email_content"])
        self.assertTrue(saved_email[0]["email_subject"]==data["email_subject"])

        db.session.query(Email).filter(Email.email_subject==data["email_subject"]).delete()
        db.session.commit()



if __name__ == '__main__':
    unittest.main()

