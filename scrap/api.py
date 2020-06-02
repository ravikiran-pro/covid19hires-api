from flask import Flask, jsonify,request
from flask_cors import CORS,cross_origin
import backend
import json

app = Flask(__name__)
CORS(app)


@app.route('/api/register', methods=['GET','POST'])
def add_new_user():
    jsonresponse=request.get_json()
    status=backend.add_user(jsonresponse)
    return json.dumps(status)

@app.route('/api/check_availablity',methods=["GET","POST"])
def checkavailablity():
    jsonresponse=request.get_json()
    status={'email':False,'aadhar':False}
    if(backend.check_email(jsonresponse["email"]) == 0):
        status["email"]=True
    if(backend.check_aadhar(jsonresponse["aadhar"]) == 0):
        status["aadhar"]=True
    return json.dumps(status)

@app.route('/api/login',methods=['GET','POST'])
def log_user_in():
    jsonresponse=request.get_json()
    status={'status':False,'sessionid':''}
    if(backend.login(jsonresponse)):
        status['sessionid']=backend.create_keygen(jsonresponse)
        status['status']=True
    return json.dumps(status)

if __name__ == '__main__':
    app.run(debug=True)
