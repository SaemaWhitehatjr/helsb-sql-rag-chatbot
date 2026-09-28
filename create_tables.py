from app.database.postgres import get_connection

connection = get_connection()

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id SERIAL PRIMARY KEY,
    student_name VARCHAR(100),
    loan_amount NUMERIC(10,2),
    status VARCHAR(50)
);
""")

connection.commit()

print("Table created successfully")

cursor.close()
connection.close()