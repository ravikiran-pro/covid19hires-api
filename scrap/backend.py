from connector import connector
import json
import pymysql

def add_user(userid):
    try:
        conn=connector()
        status={'status':False}
        query="insert into users values {}".format(tuple(userid.values())) 
        connect=conn.cursor()
        connect.execute(query)
        conn.commit()
        conn.close()
        status['status']=True
    except:
        status['status']=False
    finally:
        return status

def check_email(emailid):
    conn=connector()
    query="select * from users where email='{}'".format(emailid)
    connect=conn.cursor()
    return connect.execute(query)    

def check_aadhar(aadharid):
    conn=connector()
    query="select * from users where aadhar='{}'".format(aadharid)
    connect=conn.cursor()
    return connect.execute(query)

def login(details):
    conn=connector()
    login_datas=tuple(details.values())
    query="select * from users where email='{}' and password='{}'".format(login_datas[0],login_datas[1])
    connect=conn.cursor()
    return connect.execute(query)

def create_keygen(details):
    conn=connector()
    login_datas=tuple(details.values())
    import secrets
    key=secrets.token_urlsafe(16)
    query="insert into loggeduser values('{}','{}')".format(login_datas[0],key)
    connect=conn.cursor()
    connect.execute(query)
    conn.commit()
    conn.close()
    return key

