import mysql.connector

mycon = mysql.connector.connect(host="localhost", passwd="rootmysql",user="root")
mysql_cursor = mycon.cursor()

mysql_cursor.execute('CREATE DATABASE IF NOT EXISTS kcg')
mysql_cursor.execute('USE kcg')

query_create_table = 'CREATE TABLE dobs(id int primary key, dob varchar(8) not null)'

try:
    mysql_cursor.execute(query_create_table)
except:
    None



class discord:
    token = 'MTA0MzM4MDA3NTc5MTM4NDU4Ng.G1a8ns.7UbXHuZjH4Ou2T5t8vjUpZIlgCec9qp255fR18'

