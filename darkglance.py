import mysql.connector

mycon = mysql.connector.connect(host="localhost", passwd="rootmysql",user="root")
mysql_cursor = mycon.cursor()

mysql_cursor.execute('CREATE DATABASE IF NOT EXISTS kcg')
mysql_cursor.execute('USE kcg')

query1 = 'CREATE TABLE role_owner(name varchar(30) primary key)'
query2 = 'CREATE TABLE role_admin(name varchar(30) primary key)'
query3 = 'CREATE TABLE auth_all(value varchar(6) primary key)'
query4 = "INSERT INTO auth_all VALUES('False')"

try:
    mysql_cursor.execute(query1)
except:
    pass
    
try:
    mysql_cursor.execute(query2)
except:
    pass

try:
    mysql_cursor.execute(query3)    
except:
    pass
try:
    mysql_cursor.execute(query4)
    mysql_cursor.execute('COMMIT')

except:
    pass

class discord_:
    token = 'MTA0MzM4MDA3NTc5MTM4NDU4Ng.G1a8ns.7UbXHuZjH4Ou2T5t8vjUpZIlgCec9qp255fR18'
    
    roles = ('owner', 'admin')

    def check_authorization(channel, role):
        if not role == 'owner':
            mysql_cursor.execute('select * from auth_all')
            value = mysql_cursor.fetchone()[0]
            if value == 'True':
                return True
            else:
                pass

        author = str(channel.message.author)
        mysql_cursor.execute("select * from role_{} where name = '{}'".format(role, author))
        users = mysql_cursor.fetchall()
        try:
            if author in users[0]:
                return True
            else:
                mysql_cursor.execute('select * from auth_all')
                value = mysql_cursor.fetchone()[0]
                print(value)
                if value == 'True':
                    return True
                else:
                    return False
        except:
            return False
    
    def authorize(user_name, role):
        mysql_cursor.execute("INSERT INTO role_{} VALUES('{}')".format(role, user_name))
        mysql_cursor.execute('commit')
    
    def revoke(user_name, role):
        
        mysql_cursor.execute("select * from role_{} where name = '{}'".format(role, user_name))
        users = mysql_cursor.fetchall()
        if users == []:
            raise Exception
        else:
            pass
        
        mysql_cursor.execute("DELETE FROM role_{} WHERE name = '{}';".format(role, user_name))
        mysql_cursor.execute('commit')
    
    def auth_all():
        mysql_cursor.execute("UPDATE auth_all SET value = 'True'")
        mysql_cursor.execute('commit')
    
    def rev_all():
        mysql_cursor.execute("UPDATE auth_all SET value = 'False'")
        mysql_cursor.execute('commit')
        