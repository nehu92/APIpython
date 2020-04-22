import mysql.connector as mysql

##conecting to the dbase

db = mysql.connect( 
    host = "localhost",
    user = "root",
    passwd = "peronismo",
    database = "mydb"
)

cursor = db.cursor()
cursor.execute("SHOW TABLES")

tables = cursor.fetchall() ## it returns list of tables present in the database

## showing all the tables one by one
for table in tables:
    print(table)