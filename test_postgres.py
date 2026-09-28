from app.database.postgres import get_connection


connection = get_connection()

cursor = connection.cursor()

cursor.execute("SELECT version();")

result = cursor.fetchone()

print(result)

cursor.close()
connection.close()