import psycopg2
import sqlite3
connection=sqlite3.connect('../app/hiring')
cursor=connection.cursor()
cursor.execute("select * from data")
result=cursor.fetchone()
print(result)

connection=psycopg2.connect(
	database="ddqkh4cnlh198f",
        user="hjzobttbrnewds",
        password="3fafe193c0c99642e868fd42f28a807d0b2da619db95a85367030349a0528bf1",
        host="ec2-3-222-30-53.compute-1.amazonaws.com",
        port="5432"
        )
'''
'''
cursor=connection.cursor()
cursor.execute("select * from data");
for i in cursor.fetchall():
	print(i)
#cursor.execute("CREATE TABLE data(sno int primary key,company varchar(100),location varchar(100),role varchar(60),type varchar(30),sector varchar(50),link varchar(200));")
"""query="insert into data values({},'{}','{}','{}','{}','{}','{}')"
cursor.execute("select * from data")
result=cursor.fetchall()
for i in range(0,len(result)):
        cursor.execute(query.format(result[i][0],result[i][1],result[i][2],result[i][3],result[i][4],result[i][5],result[i][6]))
                                connection.commit()
        print(result[i][0],result[i][1])
"""
