from app.database.postgres import get_connection


def get_all_students():

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute("""
    SELECT *
    FROM students
    """)

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return rows