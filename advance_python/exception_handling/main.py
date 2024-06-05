"""
Exception handling is implemented using the try, except, else, and finally blocks. Here is an overview of each component and how they work together:

Key Components:

try block: The code that might raise an exception is placed inside a try block. This allows the program to "try" running the code and catch any exceptions that occur.

except block: This block is used to catch and handle the exceptions. If an exception occurs in the try block, the flow of control is transferred to the except block.

else block: This optional block is executed if no exceptions are raised in the try block.

finally block: This optional block is always executed, whether an exception occurred or not, and is typically used for cleanup actions (e.g., closing files or releasing resources).

assert: The assert statement is used for debugging purposes. It tests a condition, and if the condition is False, it raises an AssertionError with an optional error message.

Key Components of assert:
------------------------
- Condition: The condition that is being tested. If it evaluates to True, the program continues running normally. If it evaluates to False, an AssertionError is raised.

- Optional Message: An optional message that provides additional information about the assertion error.


Raise : The raise statement is used to raise an exception intentionally. It can be used to signal that an error condition has occurred.


Key Components of raise:
-----------------------
- Exception: The exception to be raised. This can be a built-in exception or a user-defined exception.

- Optional Arguments: Additional information or arguments that can be passed to the exception.

"""

# print("start")
# try:
#     b = int(input("Enter a b: "))
#     a = 10/b
#     print(a)
# except ZeroDivisionError:
#     print("You can not set 0 for division")
# except TypeError:
#     print("You can only divide by number values")
# except NameError:
#     print("something is not define.")
# except Exception as err:
#     print(f"ERROR : {err}")
# print("end")

# filename = "example3.txt"
# try:
#     file = open(filename, 'x')
#     print(f"{filename} has been created successfully.")
# except FileExistsError:
#     print(f"{filename} already exists.")
# except Exception as err:
#     print(f"ERROR: {err}")
# else:
#     data = "This is a python code with file handling"
#     file.write(data)
# finally:
#     file.close()
#     print("I will be print anyway")

# def divide(a, b):
#     assert b != 0, "The denominator must not be zero."
#     return a / b

# print(divide(10, 2))  # This will work and print 5.0
# print(divide(10, 0))  # This will raise an AssertionError with the message

try:
    bal = 2000
    withdrow = float(input("Enter withdrow amount: "))
    if withdrow > bal:
        raise ValueError("Insufficient balance.")
    else:
        bal -= withdrow
        print(f"Your remaining amount is : {bal}")
except ValueError:
    print("You can not withdrow balance grater than bank balance")
except Exception as err:
    print(f"ERROR: {err}")