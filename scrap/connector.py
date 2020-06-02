import pymysql

def connector():
    connection=pymysql.connect(
                'localhost',
                'root',
                'Ravikiran@ms1',
                'GoSafe')
    return connection
