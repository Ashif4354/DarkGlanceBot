import mysql.connector
import discord
import requests
####################################################################################################################################################
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


#############################################################################################################################################################

dbconnect('darkglancebot')

queries = {
    'query1' : 'CREATE TABLE role_owner(name varchar(30) primary key)',
    'query2' : 'CREATE TABLE role_admin(name varchar(30) primary key)',
    'query3' : 'CREATE TABLE auth_all(value varchar(6) primary key)',
    #'query4' : "INSERT INTO auth_all VALUES('False')",
    #'query5' : "INSERT INTO role_owner value('DarkGlance#6849')",
    'query6' : 'CREATE TABLE block_list(name varchar(30) primary key)',
    'query7' : 'CREATE TABLE dobs(id varchar(13) primary key, dob varchar(8) not null)',
    #'query8' : 'CREATE TABLE gang_members(roll_no varchar(8) primary key, name varchar(30), discord_id varchar(30), role varchar(20))'
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


#print("in __init__")