import mysql.connector 


def get_connection():
    connection = mysql.connector.connect(
       host="localhost",
       port="3306",
       user="user",
       password="password123",
       database="cheemsdb"
        )
    
    return connection