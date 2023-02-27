import os
import json
import smtplib, ssl

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_mail(ch, method, properties, body):
    
    sender_email = os.getenv("SENDER_EMAIL")
    password = os.getenv("SENDER_PASSWORD")
    body =  json.loads(body)
    subject = body["email_subject"]
    receiver = body["receiver"]
    email_content = body["email_content"]
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver


    # Turn these into plain/html MIMEText objects
    part = MIMEText(email_content, "plain")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver, message.as_string()
        )