from app.database.postgres import get_connection

connection = get_connection()

cursor = connection.cursor()

cursor.execute(
    """
    INSERT INTO students
    (
        student_name,
        loan_amount,
        status
    )
    VALUES
    (
        %s,
        %s,
        %s
    )
    """,
    (
        "John Doe",
        5000.00,
        "Active"
    )
)

connection.commit()

print("Student inserted successfully")

cursor.close()
connection.close()
