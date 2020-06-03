import sys
from flask import Flask, jsonify,request,render_template
from flask_mail import Mail,Message
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku
import json
import os

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///hiring'
#heroku=Heroku(app)
db=SQLAlchemy(app)
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

class Jobs(db.Model):
    __tablename__="data"
    sno=db.Column(db.Integer,primary_key=True)
    company=db.Column(db.String(100))
    location=db.Column(db.String(100))
    role=db.Column(db.String(60))
    type=db.Column(db.String(30))
    sector=db.Column(db.String(50))
    link=db.Column(db.String(200))

    def __init__(self,sno,company,location,role,type,sector,link):
        self.sno=sno
        self.company=company
        self.location=location
        self.role=role
        self.type=type
        self.sector=sector
        self.link=link

    def __repr__(self):
        return '{'+"sno:{},company:{}".format(self.sno,self.company)+'}'

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

@app.route('/commit')
def commit():
    job=Jobs(sno=3019,company="livewire",location="chennai",role="trainer",type="full",sector="teaching",link="support.livewire.com")
    db.session.add(job)
    db.session.commit()
    return "Data added sucessfull"

@app.route('/')
@app.route('/Home')
def get_tasks():
    res=Jobs.query.limit(10).all()
    return render_template("index.html",result=res)

if __name__ == '__main__':
    app.run(debug=True)


