import mysql.connector
import discord

value_name =  'Fetches the Name of the student \n This command can be used by all user'
value_marks = 'Fetches Marks of the student \n This command can be used by all users'
value_registernumber = 'Fetches Register number of the student \n This command can be used by all users'
value_rollnumber = 'Fetches Roll number of the student \n This command can be used by all users'
value_dob =  'Fetches the Date of birth of the student \n This command can be used by authorized users only'
value_photo = 'Fetches the Photo of the student \n This command can be used by authorized users only'
value_details = 'Fetches Details of the student \n This command can be used by authorized users only'
value_all = 'Fetches All details of the student(photo, details, marks) together \n This command can be used by authorized users only'
embed_description = '''All available commands
Note : This BOT can only handle one request at a time
Some request may take longer time to fetch data because dob cracking is a lengthy process
So Please wait.. It wont take more than a minute in most cases

ALL THE COMMANDS ARE LISTED BELOW'''

help_embed = discord.Embed(title = 'DarkGlanceBot Help',color = 0xffffff, description  = embed_description)
help_embed.add_field(name = '.kcgstudent name <reg_no / roll_no>', value = value_name, inline = False)
help_embed.add_field(name = '.kcgstudent marks <reg_no / roll_no>', value = value_marks, inline = False)
help_embed.add_field(name = '.kcgstudent registernumber <reg_no / roll_no>', value = value_registernumber, inline = False)
help_embed.add_field(name = '.kcgstudent rollnumber <reg_no / roll_no>', value = value_rollnumber, inline = False)
help_embed.add_field(name = '.kcgstudent dob <reg_no / roll_no>', value = value_dob, inline = False)
help_embed.add_field(name = '.kcgstudent photo <reg_no / roll_no>', value = value_photo, inline = False)
help_embed.add_field(name = '.kcgstudent details <reg_no / roll_no>', value = value_details, inline = False)
help_embed.add_field(name = '.kcgstudent all <reg_no / roll_no>', value = value_all, inline = False)
help_embed.set_footer(text = 'DarkGlanceBOT is just made for educational/testing purpose, So please dont misuse')


mycon = None
mysql_cursor = None

class db:   
    def db_con():
        global mycon, mysql_cursor
        mycon = mysql.connector.connect(host="localhost", passwd="rootmysql",user="root")
        mysql_cursor = mycon.cursor() 
        mysql_cursor.execute('CREATE DATABASE IF NOT EXISTS kcg')
        mysql_cursor.execute('USE kcg')   

    

query1 = 'CREATE TABLE role_owner(name varchar(30) primary key)'
query2 = 'CREATE TABLE role_admin(name varchar(30) primary key)'
query3 = 'CREATE TABLE auth_all(value varchar(6) primary key)'
#query4 = "INSERT INTO auth_all VALUES('False')"
#query5 = "INSERT INTO role_owner value('DarkGlance#6849')"

db.db_con()
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
"""
try:
    mysql_cursor.execute(query4)
    mysql_cursor.execute(query5)
    mysql_cursor.execute('COMMIT')
except:
    pass
"""

db.db_con()

class discord_:
    token = 'MTA0MzM4MDA3NTc5MTM4NDU4Ng.G1a8ns.7UbXHuZjH4Ou2T5t8vjUpZIlgCec9qp255fR18'
    
    roles = ('owner', 'admin')
    
    def check_authorization(ctx, role):
        if not role == 'owner':
            mysql_cursor.execute('select * from auth_all')
            value = mysql_cursor.fetchone()[0]
            if value == 'True':
                return True
            else:
                pass

        author = str(ctx.message.author)
        mysql_cursor.execute("select * from role_{} where name = '{}'".format(role, author))
        users = mysql_cursor.fetchall()
        try:
            if author in users[0]:
                return True
            else:
                return False
        except:
            return False
    
    def authorize(user_name, role):
        mysql_cursor.execute("select * from role_{} where name = '{}'".format(role, user_name))
        users = mysql_cursor.fetchall()
        if users != []:
            raise Exception
        else:
            pass

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
        