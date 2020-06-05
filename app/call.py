from flask_mail import Mail,Message
import app.main

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///hiring'
mail_settings={
    "MAIL_SERVER":"smtp.gmail.com",
    "MAIL_PORT":465,
    "MAIL_USE_TLS":False,
    "MAIL_USE_SSL":True,
    "MAIL_USERNAME":"proraviki@gmail.com",
    "MAIL_PASSWORD":"412515120301"
}
app.config.update(mail_settings)
mail=Mail(app)

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
