from app.config import app,db
from flask import render_template,jsonify,session,request
from app.model import Jobs,JobsSchema
from app.mail import send_otp
from flask_json import as_json
@app.route('/Login')
def commit():
    #job=Jobs(sno=3019,company="livewire",location="chennai",role="trainer",type="full",sector="teaching",link="support.livewire.com")
    #db.session.add(job)
    #db.session.commit()

    '''set session'''
    #import secrets
    #session["hiretohire"]=secrets.token_urlsafe(20)
    '''check session presence'''
    if "hiretohire" in session:
        cd=session["hiretohire"]
        print(cd)
    '''season pop'''
    #session.pop('hiretohire',None)

    return "Data added sucessfull"

@app.route('/api/dropdown/type',methods=['POST'])
def getCompanies():
    res=db.session.query(Jobs.type).distinct().all()
    user_schema=JobsSchema(many=True)
    output=user_schema.dump(res)
    return jsonify({'output':output})

@app.route('/api/dropdown/location',methods=['POST'])
def getLocation():
    res=db.session.query(Jobs.location).distinct().all()
    user_schema=JobsSchema(many=True)
    output=user_schema.dump(res)
    return jsonify({'output':output})

@app.route('/api/dropdown/role',methods=['POST'])
def getRoles():
    res=db.session.query(Jobs.role).distinct().all()
    user_schema=JobsSchema(many=True)
    output=user_schema.dump(res)
    return jsonify({'output':output})

@app.route('/api/dropdown/sector',methods=['POST'])
def getSectors():
    res=db.session.query(Jobs.sector).distinct().all()
    user_schema=JobsSchema(many=True)
    output=user_schema.dump(res)
    return jsonify({'output':output})

@app.route('/api/all',methods=['POST'])
def get_task():
    form=request.get_json()
    start=int(form["start"])
    end=int(form["end"])
    res=db.session.query(Jobs.company,Jobs.role,Jobs.location,Jobs.link).filter(Jobs.sno>start,Jobs.sno<end)
    user_schema=JobsSchema(many=True)
    output=user_schema.dump(res)
    return jsonify(output)
    return jsonify({'user':output})

@app.route('/register',methods=['GET','POST'])
def new_user():
    print(request.data)
    #import secrets
    #session["hiretohire"]=secrets.token_urlsafe(20)
    if "hiretohire" in session:
        cd=session["hiretohire"]
        print(cd)
    return 'alert("data sucessfull")'

@app.route('/')
def hello():
    return "working"
