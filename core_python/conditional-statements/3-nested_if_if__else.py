"""
syntax :

if (condition-1):
    if (condition-2):
        block of code
    else:
        block of code
else:
    block of code
"""


age = int(input("Enter age: "))


if age >= 18:
    weight = int(input("Enter weight: "))
    if (weight >= 50):
        print("You can donate")
    else:
        print("You can not donate.")
else:
    print("You can not donate.")