from app.config import app,db
from flask import render_template,jsonify
from app.model import Jobs,JobsSchema


@app.route('/commit')
def commit():
    job=Jobs(sno=3019,company="livewire",location="chennai",role="trainer",type="full",sector="teaching",link="support.livewire.com")
    db.session.add(job)
    db.session.commit()
    return "Data added sucessfull"

@app.route('/api/all')
def get_all_results():
    res=Jobs.query.limit(10).all()
    user_schema=JobsSchema(many=True)
    output=user_schema.dump(res)
    return jsonify({'user':output})

@app.route('/api/company-names',methods=['POST'])
def get_tasks():
    res=db.session.query(Jobs.role).distinct().limit(10)
    user_schema=JobsSchema(many=True)
    output=user_schema.dump(res)
    return jsonify({'output':output})

@app.route('/')
def get_task():
    res=db.session.query(Jobs.company).limit(10)
    user_schema=JobsSchema(many=True)
    output=user_schema.dump(res)
    return render_template("index.html",result=jsonify({'user':output}))
