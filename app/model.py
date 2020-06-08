from app.config import db
from marshmallow_sqlalchemy import ModelSchema

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
        self.list=[]

class JobsSchema(ModelSchema):
    class Meta:
        model=Jobs
