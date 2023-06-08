import mysql.connector
from mysql.connector import Error


# connect to mysql
cnx = mysql.connector.connect(
    user='projectmanager', # create a user first before running
    password='project',
    host='localhost',  
    database='proj'  # replace database name if needed
)

cursor = cnx.cursor() 

# import mysql.connector
# from mysql.connector import Error
# from mysql.connector import errorcode

# db = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root"
# )