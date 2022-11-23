import mysql.connector

mycon = mysql.connector.connect(host="localhost", passwd="rootmysql",user="root")
mysql_cursor = mycon.cursor()

mysql_cursor.execute('CREATE DATABASE IF NOT EXISTS kcg')
mysql_cursor.execute('USE kcg')

query1 = 'CREATE TABLE role_owner(name varchar(30))'
query2 = 'CREATE TABLE role_admin(name varchar(30))'

try:
    mysql_cursor.execute(query1)
except:
    None
    
try:
    mysql_cursor.execute(query2)
except:
    None

class discord_:
    token = 'MTA0MzM4MDA3NTc5MTM4NDU4Ng.G1a8ns.7UbXHuZjH4Ou2T5t8vjUpZIlgCec9qp255fR18'
    
    roles = ('owner', 'admin')

    def check_authorization(channel, role):
        author = channel.message.author
        mysql_cursor.execute("select * from role_{} where name = '{}'".format(role, author))
        users = mysql_cursor.fetchone()
        if str(author) in users:
            return True
        else:
            return False
    
    def authorize(user_name, role):
        mysql_cursor.execute("INSERT INTO role_{} VALUES('{}')".format(role, user_name))
        mysql_cursor.execute('commit')

    
    def revoke(user_name, role):
        mysql_cursor.execute("DELETE FROM role_{} WHERE name = '{}';".format(role, user_name))
        mysql_cursor.execute('commit')



