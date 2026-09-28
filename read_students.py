from app.database.postgres import get_connection

connection = get_connection()

cursor = connection.cursor()

cursor.execute("""
SELECT *
FROM students
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
connection.close()