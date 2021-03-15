from app import app
from flask_mail import Mail, Message

mail = Mail(app)


def send_email(recipients: list, server_email=app.config['MAIL_DEFAULT_SENDER']) -> None:
    msg = Message("Feedback", recipients=recipients, sender=server_email)
    msg.body = f"You have received a new feedback from {server_email.split('@')[0]} <{server_email}>."
    mail.send(msg)