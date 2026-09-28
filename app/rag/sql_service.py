from app.database.student_repository import get_all_students
from app.core.tracing import traceable

@traceable(name="sql_retrieval")
def get_student_context():

    students = get_all_students()

    context = []

    for student in students:

        context.append(
            f"""
            Student ID: {student[0]}
            Name: {student[1]}
            Loan Amount: {student[2]}
            Status: {student[3]}
            """
        )

    return "\n".join(context)