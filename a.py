import mysql.connector
mycon = mysql.connector.connect(host="localhost", passwd="rootmysql",user="root")
mysql_cursor = mycon.cursor()

mysql_cursor.execute('CREATE DATABASE IF NOT EXISTS kcg')
mysql_cursor.execute('USE kcg')


global_connect_timeout = 'SET GLOBAL connect_timeout=180'
global_wait_timeout = 'SET GLOBAL wait_timeout=180'
global_interactive_timeout = 'SET GLOBAL interactive_timeout=180'

mysql_cursor.execute(global_connect_timeout)
mysql_cursor.execute(global_wait_timeout)
mysql_cursor.execute(global_interactive_timeout)