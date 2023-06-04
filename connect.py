import mysql.connector

# connect to mysql
cnx = mysql.connector.connect(
    user='projectmanager', # create a user first before running
    password='project',
    host='localhost',  
    database='proj'  # replace database name if needed
)

cursor = cnx.cursor()