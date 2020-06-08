from app.config import app,db
from flask import render_template,jsonify,session
from app.model import Jobs,JobsSchema
from app.mail import send_otp


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

@app.route('/')
def get_task():
    send_otp()
    res=db.session.query(Jobs.company).limit(10)
    user_schema=JobsSchema(many=True)
    output=user_schema.dump(res)
    return render_template("index.html",result=jsonify({'user':output}))
