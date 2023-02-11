import mysql.connector

from sys import path
path.append(getcwd().rstrip('kcg'))
from logger.logger import logger
from darkglance import *

mycon = None
mysql_cursor = None

class db:
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


class gang:
    pass