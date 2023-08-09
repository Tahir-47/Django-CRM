import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'Tahir',
    passwd = '12345'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crmDB")

print("All done!")