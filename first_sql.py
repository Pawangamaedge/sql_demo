import mysql.connector as mysql
db = mysql.connect(
    host = "localhost",
    user = "root",
    password="12da12",
    database="new_database_demo"
)
my_cursor=db.cursor()
# my_cursor.execute("CREATE DATABASE new_database_demo") # creates the data base
# my_database_table=my_cursor.execute("show databases")  # shows the data base
# tables=my_cursor.execute("create table customer (name varchar(225), address varchar(225))")
my_cursor.execute("show tables") # showes table
for x in my_cursor:
     print(x)
