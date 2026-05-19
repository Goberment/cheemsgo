from persistence.db import get_connection
 
class Trip:
 
    def __init__(self, name: str, city: str, latitude: float, longitude: float):
        self.name = name
        self.city = city
        self.latitude = latitude
        self.longitude = longitude
 
    def get_all():
        connection = None
        cursor = None
        try:
            connection = get_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT id, name, city, latitude, longitude FROM trip")
            return cursor.fetchall()
        finally:
            if cursor: cursor.close()
            if connection: connection.close()
 
    def get_one(trip_id: int):
        connection = None
        cursor = None
        try:
            connection = get_connection()
            cursor = connection.cursor(dictionary=True)
            cursor.execute(
                "SELECT id, name, city, latitude, longitude FROM trip WHERE id = %s",
                (trip_id,)
            )
            return cursor.fetchone()
        finally:
            if cursor: cursor.close()
            if connection: connection.close()
 
    def save(self):
        connection = None
        cursor = None
        try:
            connection = get_connection()
            cursor = connection.cursor()
            sql = 'INSERT INTO trip (name, city, latitude, longitude) VALUES (%s, %s, %s, %s)'
            cursor.execute(sql, (self.name, self.city, self.latitude, self.longitude))
            connection.commit()
            return cursor.lastrowid
        finally:
            if cursor: cursor.close()
            if connection: connection.close()
 
    def update(self, trip_id: int):
        connection = None
        cursor = None
        try:
            connection = get_connection()
            cursor = connection.cursor()
            sql = 'UPDATE trip SET name = %s, city = %s, latitude = %s, longitude = %s WHERE id = %s'
            cursor.execute(sql, (self.name, self.city, self.latitude, self.longitude, trip_id))
            connection.commit()
            return cursor.rowcount
        finally:
            if cursor: cursor.close()
            if connection: connection.close()
 
    def delete(trip_id: int):
        connection = None
        cursor = None
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("DELETE FROM trip WHERE id = %s", (trip_id,))
            connection.commit()
            return cursor.rowcount
        finally:
            if cursor: cursor.close()
            if connection: connection.close()
 