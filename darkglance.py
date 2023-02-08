import mysql.connector
import discord
import requests

#############################################################################################################################################################
#############################################################################################################################################################
value_name =  'Fetches the Name of the student \nThis command can be used by all user'
value_marks = 'Fetches Marks of the student \nThis command can be used by all users'
value_registernumber = 'Fetches Register number of the student \nThis command can be used by all users'
value_rollnumber = 'Fetches Roll number of the student \nThis command can be used by all users'
value_dob =  'Fetches the Date of birth of the student \nThis command can be used by authorized users only'
value_photo = 'Fetches the Photo of the student \nThis command can be used by authorized users only'
value_details = 'Fetches Details of the student \nThis command can be used by authorized users only'
value_all = 'Fetches All details of the student(photo, details, marks) together \nThis command can be used by authorized users only'
value_search = 'Searches for students with keyword \nThis command can be used by authorized users only'
value_np = 'Fetches the Name and Photo of the student \nThis command can be used by authorized users only'

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
help_embed.add_field(name = '.kcgstudent namephoto <reg_no / roll_no>', value = value_np, inline = False)
help_embed.add_field(name = '.kcgstudent details <reg_no / roll_no>', value = value_details, inline = False)
help_embed.add_field(name = '.kcgstudent all <reg_no / roll_no>', value = value_all, inline = False)
help_embed.add_field(name = '.kcgsearch <year> <keyword> <department>', value = value_search, inline = False)
help_embed.set_footer(text = 'DarkGlanceBOT is just made for educational/testing purpose, So please don\'t misuse')
#############################################################################################################################################################
#############################################################################################################################################################

error_message = '''- College server timed out
- College server down
'''

server_error_embed = discord.Embed(title = 'Some error has occured',color = 0xffffff)
server_error_embed.add_field(name = 'This may be due to the following reasons', value = error_message, inline = False)

#############################################################################################################################################################
#############################################################################################################################################################
mycon = None
mysql_cursor = None

def dbconnect():
    global mycon, mysql_cursor

    mycon = mysql.connector.connect(host='localhost', passwd='rootmysql',user='root', autocommit = True)
    mysql_cursor = mycon.cursor() 
    mysql_cursor.execute('CREATE DATABASE IF NOT EXISTS kcg')
    mysql_cursor.execute('USE kcg')  

def dbdisconnect():
    global mycon, mysql_cursor
    
    mysql_cursor.close()
    mycon.close()


#############################################################################################################################################################
#############################################################################################################################################################
#user defined exceptions

class Blocked(Exception):
    pass

class NegativeNumber(Exception):
    pass

class InvalidDelay(Exception):
    pass


#############################################################################################################################################################
#############################################################################################################################################################

dbconnect()

queries = {
    'query1' : 'CREATE TABLE role_owner(name varchar(30) primary key)',
    'query2' : 'CREATE TABLE role_admin(name varchar(30) primary key)',
    'query3' : 'CREATE TABLE auth_all(value varchar(6) primary key)',
    #'query4' : "INSERT INTO auth_all VALUES('False')",
    #'query5' : "INSERT INTO role_owner value('DarkGlance#6849')",
    'query6' : 'CREATE TABLE block_list(name varchar(30) primary key)',
    'query7' : 'CREATE TABLE dobs(id varchar(13) primary key, dob varchar(8) not null)'
}

for query in queries:
    try:
        mysql_cursor.execute(queries[query])
    except:
        pass

dbdisconnect()

#############################################################################################################################################################
#############################################################################################################################################################

server_status_embed = discord.Embed(title = 'KCG Server status', color = 0xffffff)

class kcg_:
    def check_server():
        
        server_status_embed = discord.Embed(title = 'KCG Server status', color = 0xffffff)

        fees_url = 'http://studentonlinepayment.kcgcollege.ac.in/'
        student_login_url = 'http://studentlogin.kcgcollege.ac.in/'

        fees_login_payload = {
            '__EVENTTARGET' : '' ,
            '__EVENTARGUMENT' : '',
            '__LASTFOCUS' : '',
            '__VIEWSTATE' : '/wEPDwUKMTQ4NjQwMTIzNw9kFgICAw9kFgoCCQ8QDxYGHg1EYXRhVGV4dEZpZWxkBQhjb2xsbmFtZR4ORGF0YVZhbHVlRmllbGQFDGNvbGxlZ2VfY29kZR4LXyFEYXRhQm91bmRnZBAVARlLQ0cgQ29sbGVnZSBvZiBUZWNobm9sb2d5FQECMTMUKwMBZxYBZmQCCw8QZBAVAgtSb2xsIE51bWJlcg9SZWdpc3RlciBOdW1iZXIVAgEwATEUKwMCZ2cWAWZkAg0PD2QWBB4LcGxhY2Vob2xkZXIFC1JvbGwgTnVtYmVyHgxhdXRvY29tcGxldGUFA29mZmQCEQ8PFgIeB1Zpc2libGVoFgIfBAUDb2ZmZAIVDw8WAh8FaGRkZNW+28hPSHWELbHwTZyc+FgrCQj/p6TzJx0gJo3tNhyA', 
            '__VIEWSTATEGENERATOR' : 'CA0B0334',
            '__EVENTVALIDATION' : '/wEdAAa5cfVM3pWzdu9rE2vQn04A1ewWtm3evXPJ0S9N/1pup/olUdBTEtKbUYVn9qLUVnP36l7NJf9XLe0xTP1byily7ATayzSAKKfWGUr2Dqcb+c34O/GfAV4V4n0wgFZHr3fbr4+GviYj6YKdFlGPdh5Q23daRHDXkik+zyEsEtmUSg==',
            'rblOnlineAppLoginMode' : '0',
            'txtuname' : '20cs001',
            'Button1' : 'Login'
            }

        student_login_payload = {
            '__EVENTTARGET' : '' ,
            '__EVENTARGUMENT' : '',
            '__LASTFOCUS' : '',
            '__VIEWSTATE' : '/wEPDwUJMjkwMTA2NTY5D2QWAgIDD2QWCgIDDxAPFgYeDURhdGFUZXh0RmllbGQFCGNvbGxuYW1lHg5EYXRhVmFsdWVGaWVsZAUMY29sbGVnZV9jb2RlHgtfIURhdGFCb3VuZGdkEBUBGUtDRyBDb2xsZWdlIG9mIFRlY2hub2xvZ3kVAQIxMxQrAwFnFgFmZAIFDxBkEBUCC1JvbGwgTnVtYmVyEVJlZ2lzdGVyZWQgTnVtYmVyFQIBMAExFCsDAmdnFgFmZAIHDw9kFgQeC3BsYWNlaG9sZGVyBQtSb2xsIE51bWJlch4MYXV0b2NvbXBsZXRlBQNvZmZkAgsPD2QWAh8EBQNvZmZkAg8PDxYCHgdWaXNpYmxlaGRkZEUh8Q9VeEnmpvJTjWVIwQmtVpX5IBYcjkAZZqWYNv5m', 
            '__VIEWSTATEGENERATOR' : 'CA0B0334',
            '__EVENTVALIDATION' : '/wEdAAfEhVpMiIC9PlqrGxNesSta1ewWtm3evXPJ0S9N/1pup/olUdBTEtKbUYVn9qLUVnP36l7NJf9XLe0xTP1byily7ATayzSAKKfWGUr2Dqcb+ZxpWckI3qdmfEJVCu2f5cHN+DvxnwFeFeJ9MIBWR6935FJfAFbS62yyYTlq6hIkdlrWUyRFAO0MmBe4dmPHJe8=',
            'rblOnlineAppLoginMode' : '0',
            'txtuname' : '20cs008',
            'txtpassword' : '25112002',
            'Button1' : 'Login'
            }
        try:
            page = requests.get(fees_url, timeout = 3)
            server_status_embed.add_field(name = 'Fees Login page', value = 'Positive', inline = False)
        except Exception:
            server_status_embed.add_field(name = 'Fees Login page', value = 'Negative', inline = False)

        try:
            page = requests.post(fees_url, data = fees_login_payload, timeout = 3)
            server_status_embed.add_field(name = 'Fees Login', value = 'Positive', inline = False)
        except Exception:
            server_status_embed.add_field(name = 'Fees Login', value = 'Negative', inline = False)
        
        try:
            page = requests.get(student_login_url, timeout = 3)
            server_status_embed.add_field(name = 'Student Login page', value = 'Positive', inline = False)
        except Exception:
            server_status_embed.add_field(name = 'Student Login page', value = 'Negative', inline = False)

        try:
            page = requests.post(student_login_url, data = student_login_payload, timeout = 3)
            server_status_embed.add_field(name = 'Student Login', value = 'Positive', inline = False)
        except Exception:
            server_status_embed.add_field(name = 'Student Login', value = 'Negative', inline = False)
        
        return server_status_embed
            

#############################################################################################################################################################
#############################################################################################################################################################

class discord_:
    token = 'MTA0MzM4MDA3NTc5MTM4NDU4Ng.G1a8ns.7UbXHuZjH4Ou2T5t8vjUpZIlgCec9qp255fR18'
    
    roles = ('owner', 'admin')
    
    def check_authorization(ctx, role):
        dbconnect()

        mysql_cursor.execute("SELECT * FROM block_list where name = '{}'".format(ctx.message.author))
        if mysql_cursor.fetchall() == []:
            pass
        else:
            raise Blocked

        if not role in discord_.roles:
            mysql_cursor.execute('select * from auth_all')
            value = mysql_cursor.fetchone()[0]
            if value == 'True':
                dbdisconnect()
                return True
            else:
                pass

        author = str(ctx.message.author)
        mysql_cursor.execute("select * from role_{} where name = '{}'".format(role, author))
        users = mysql_cursor.fetchall()
        try:
            if author in users[0]:
                dbdisconnect()
                return True
            else:
                dbdisconnect()
                return False
        except:
            return False
    
    def authorize(user_name, role):
        dbconnect()
        mysql_cursor.execute("select * from role_{} where name = '{}'".format(role, user_name))
        users = mysql_cursor.fetchall()
        if users != []:
            raise Exception
        else:
            pass

        mysql_cursor.execute("INSERT INTO role_{} VALUES('{}')".format(role, user_name))
        dbdisconnect()
    
    def revoke(user_name, role):
        dbconnect()        
        mysql_cursor.execute("select * from role_{} where name = '{}'".format(role, user_name))
        users = mysql_cursor.fetchall()
        if users == []:
            raise Exception
        else:
            pass
        
        mysql_cursor.execute("DELETE FROM role_{} WHERE name = '{}';".format(role, user_name))
        dbdisconnect()
    
    def auth_all():
        dbconnect()
        mysql_cursor.execute("UPDATE auth_all SET value = 'True'")
        dbdisconnect()
    
    def rev_all():
        dbconnect()
        mysql_cursor.execute("UPDATE auth_all SET value = 'False'")
        dbdisconnect()
        
    def block(user_name):
        dbconnect()
        mysql_cursor.execute("INSERT INTO block_list VALUES('{}')".format(user_name))
        dbdisconnect()
    
    def unblock(user_name):
        dbconnect()
        mysql_cursor.execute("DELETE FROM block_list WHERE name = '{}';".format(user_name))
        dbdisconnect()

async def check_auth(ctx, roles, message = 'You dont have authorization to use this command'):
    try:
        for role in roles:
            if discord_.check_authorization(ctx, role):
                return True
        else:
            embed = discord.Embed(description = ctx.message.author.mention + message, color = 0xffffff)
            await ctx.send(embed = embed)
            return False

    except Blocked:
        embed = discord.Embed(title = 'YOU ARE BLOCKED', description = 'Contact DarkGlance#6849 for queries', color = 0xffffff)
        await ctx.send(embed = embed)
        return False




#############################################################################################################################################################
#############################################################################################################################################################