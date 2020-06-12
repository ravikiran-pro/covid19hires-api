from app.config import app,db
from flask import render_template,jsonify,session,request,url_for,redirect
from app.model import Jobs,JobsSchema
from app.mail import send_otp
from flask_json import as_json
from sqlalchemy.sql import text
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

@app.route('/register',methods=['GET','POST'])
def new_user():
    print(request.data)
    #import secrets
    #session["hiretohire"]=secrets.token_urlsafe(20)
    if "hiretohire" in session:
        cd=session["hiretohire"]
        print(cd)
    return 'alert("data sucessfull")'

def get_searchResults(form):
    del form["start"]
    query=''
    for key,value in form.items():
        if value is not '':
            query+="{}='{}'".format(key,value)
            query+=" AND "
    query=query[:-4]
    return query

def Reverse_Dictlist(list):
    revlist=[]
    for i in range(len(list)-1,-1,-1):
        revlist.append(list[i])
    return revlist

@app.route('/api/searchresults/forwards',methods=['POST'])
def forward():
    form=request.get_json()
    start=form["start"] 
    query=get_searchResults(form)
    res=db.session.query(Jobs.sno,Jobs.company,Jobs.role,Jobs.location,Jobs.link).filter(text(query)).filter(Jobs.sno>start).order_by(Jobs.sno.asc()).limit(4)
    user_schema=JobsSchema(many=True)
    output=user_schema.dump(res)
    return jsonify(output)

@app.route('/api/searchresults/backwards',methods=['POST'])
def BackwardSearchResults():
    form=request.get_json()
    start=form["start"]
    query=get_searchResults(form)
    res=db.session.query(Jobs.sno,Jobs.company,Jobs.role,Jobs.location,Jobs.link).filter(text(query)).filter(Jobs.sno<start).order_by(Jobs.sno.desc()).limit(4)
    user_schema=JobsSchema(many=True)
    output=user_schema.dump(res)
    return jsonify(Reverse_Dictlist(output))

@app.route('/')
def hello():
    return render_template('index.html')
