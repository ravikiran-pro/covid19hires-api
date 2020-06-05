from app.config import app,mail
from flask_mail import Message

def send_otp():
    with app.app_context():
        msg = Message(subject="Hello",
                      sender=app.config.get("MAIL_USERNAME"),
                      recipients=["proraviki@gmail.com"], # replace with your email for testing
                      body="checking otp service")
        try:
            mail.send(msg)
        except Exception as e:
            print(e)