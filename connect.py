import mysql.connector


# connect to mysql
dsn = {
    "user":'projectmanager', # create a user first before running
    "password":'project',
    "host":'localhost',  
    "database":'proj'  # replace database name if needed
}

cnx = mysql.connector.connect(**dsn)

cursor = cnx.cursor() 