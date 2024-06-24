from .dbConection import db, cursor

def create_table_func():
    sql = 'create table students(student_id int primary key auto_increment, name varchar(255), age int)'
    cursor.execute(sql)