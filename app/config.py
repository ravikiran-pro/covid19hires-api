from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku
from flask_marshmallow import Marshmallow
from flask_mail import Mail

app = Flask(__name__)
CORS(app)
app.config['debug']=True
app.config['SECRET_KEY']="37%^@sh3(&*@*#("
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///hiring'
#heroku=Heroku(app)
db=SQLAlchemy(app)
ma=Marshmallow(app)
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