from .dbConection import db, cursor

def get_all_data_func():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    for student in students:
        print(student)