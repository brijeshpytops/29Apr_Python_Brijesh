"""
syntax :

if (condition-1):
    block of code will be execute if condition-1 will be true
elif (condition-2):
    block of code will be execute if condition-2 will be true
elif (condition-3):
    block of code will be execute if condition-3 will be true
elif (condition-4):
    block of code will be execute if condition-4 will be true
elif (condition-5):
    block of code will be execute if condition-5 will be true
else:
    block of code will be execute all conditions will be false
"""

# pr = 32
# 
# if pr >= 80:
#     print("First class")
# elif pr >= 60:
#     print("Second class")
# elif pr >= 40:
#     print("Third class")
# else:
#     print("Sorry!, you are failed. better luck next time.")


pr = 101

if pr >= 0 and pr <= 100:
    if pr >= 80:
        print("First class")
    elif pr >= 60:
        print("Second class")
    elif pr >= 40:
        print("Third class")
    else:
        print("Sorry!, you are failed. better luck next time.")
else:
    print("Invalid percentage.\nPlease enter valid PR between (0 to 100)")

