from .dbConection import db, cursor


def insert_data_func():
    sql = """
    INSERT INTO students (name, age) VALUES (%s, %s)
    """
    values = [
        ('John Doe', 20),
        ('Jane Smith', 22),
        ('Michael Johnson', 19),
        ('Emily Davis', 21),
        ('Christopher Brown', 23),
        ('Jessica Wilson', 20),
        ('Matthew Jones', 22),
        ('Sarah Lee', 21),
        ('Daniel Garcia', 19),
        ('Samantha Martinez', 20)
    ]

    try:
        cursor.executemany(sql, values)
        db.commit()  # Commit the transaction
        print(f"{cursor.rowcount} records inserted successfully.")
    except Exception as e:
        db.rollback()  # Rollback in case of error
        print(f"An error occurred: {e}")

# Example usage
# insert_data_func()
