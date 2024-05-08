"""
syntax : 

if (condition):
    block of code will be execute if condition will be true
else:
    block of code will be execute if condition will be false
"""

# score = 23
# if score >= 35:
#     print("You are pass.")
# else:
#     print("Sorry!, you are failed. better luck next time.")


balance = 10000
w_bal = 20000

if w_bal <= balance:
    balance -= w_bal
    print("Your balance is : ", balance)
else:
    print("You balance is insufficent.")