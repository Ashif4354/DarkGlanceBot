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
help_embed.add_field(name = '.kcgsearch <year> <keyword> <department>', value = value_search, inline = False)
help_embed.set_footer(text = 'DarkGlanceBOT is just made for educational/testing purpose, So please dont misuse')
#############################################################################################################################################################
#############################################################################################################################################################

error_message = '''- College server down
- College server timed out
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
    'query_create_table' : 'CREATE TABLE dobs(id varchar(13) primary key, dob varchar(8) not null)'
}

for query in queries:
    try:
        mysql_cursor.execute(queries[query])
    except:
        pass

dbdisconnect()

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

        if not role == 'owner':
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