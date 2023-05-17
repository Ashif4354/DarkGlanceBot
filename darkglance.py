import mysql.connector
import discord
import requests

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

def dbconnect(db_name):
    global mycon, mysql_cursor

    mycon = mysql.connector.connect(host='localhost', passwd='rootmysql',user='root', autocommit = True)
    mysql_cursor = mycon.cursor() 
    mysql_cursor.execute(f'CREATE DATABASE IF NOT EXISTS {db_name}')
    mysql_cursor.execute(f'USE {db_name}')  

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

class GameNotAvailable(Exception):
    pass

class server_down(Exception):
    pass

class NoPhoto(Exception):
    pass

class DobNotFound(Exception):
    pass

class NotRegNum(Exception):
    pass


#############################################################################################################################################################
#############################################################################################################################################################

dbconnect('darkglancebot')

queries = {
    'query1' : 'CREATE TABLE role_owner(name varchar(30) primary key)',
    'query2' : 'CREATE TABLE role_admin(name varchar(30) primary key)',
    'query3' : 'CREATE TABLE auth_all(value varchar(6) primary key)',
    #'query4' : "INSERT INTO auth_all VALUES('True')",
    #'query5' : "INSERT INTO role_owner value('DarkGlance#6849')",
    'query6' : 'CREATE TABLE block_list(name varchar(30) primary key)',
    'query7' : 'CREATE TABLE dobs(id varchar(13) primary key, dob varchar(8) not null)',
    'query8' : 'CREATE TABLE gang_members(roll_no varchar(8) primary key, name varchar(20) not null, dob varchar(9) notnull )'
}

for query in queries:
    try:
        mysql_cursor.execute(queries[query])
    except:
        pass

dbdisconnect()
#############################################################################################################################################################
dbconnect('kcg')

queries = {
    'query' : 'CREATE TABLE dobs(id varchar(13) primary key, dob varchar(8) not null)'
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

#############################################################################################################################################################
#############################################################################################################################################################

class discord_:
    token = 'MTA0MzM4MDA3NTc5MTM4NDU4Ng.G1a8ns.7UbXHuZjH4Ou2T5t8vjUpZIlgCec9qp255fR18'
    
    roles = ('owner', 'admin')
    
    def check_authorization(ctx, role):
        dbconnect('darkglancebot')

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
        dbconnect('darkglancebot')
        mysql_cursor.execute("select * from role_{} where name = '{}'".format(role, user_name))
        users = mysql_cursor.fetchall()
        if users != []:
            raise Exception
        else:
            pass

        mysql_cursor.execute("INSERT INTO role_{} VALUES('{}')".format(role, user_name))
        dbdisconnect()
    
    def revoke(user_name, role):
        dbconnect('darkglancebot')        
        mysql_cursor.execute("select * from role_{} where name = '{}'".format(role, user_name))
        users = mysql_cursor.fetchall()
        if users == []:
            raise Exception
        else:
            pass
        
        mysql_cursor.execute("DELETE FROM role_{} WHERE name = '{}';".format(role, user_name))
        dbdisconnect()
    
    def auth_all():
        dbconnect('darkglancebot')
        mysql_cursor.execute("UPDATE auth_all SET value = 'True'")
        dbdisconnect()
    
    def rev_all():
        dbconnect('darkglancebot')
        mysql_cursor.execute("UPDATE auth_all SET value = 'False'")
        dbdisconnect()
        
    def block(user_name):
        dbconnect('darkglancebot')
        mysql_cursor.execute("INSERT INTO block_list VALUES('{}')".format(user_name))
        dbdisconnect()
    
    def unblock(user_name):
        dbconnect('darkglancebot')
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