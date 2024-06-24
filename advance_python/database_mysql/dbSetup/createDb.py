from .dbConection import db, cursor

def create_db_func():
    database_name = input("Enter a databse name: ")
    sql = f'create database {database_name}'
    cursor.execute(sql)