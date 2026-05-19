import mysql.connector
import os
 
def get_connection():
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", "goberment31"),
        database=os.getenv("DB_NAME", "cheemsdb")
    )
    return connection