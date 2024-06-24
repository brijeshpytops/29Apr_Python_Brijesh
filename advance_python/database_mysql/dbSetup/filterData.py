from .dbConection import db, cursor

def filter_data_func():
    # cursor.execute("SELECT * FROM students limit 5") # limit
    # cursor.execute("SELECT * FROM students order by name") # order by ASC
    cursor.execute("SELECT * FROM students order by name DESC") # order by DESc
    students = cursor.fetchall()
    for student in students:
        print(student)