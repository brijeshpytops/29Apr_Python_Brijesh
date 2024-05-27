# a = 10
# b = 20
# c = a + b
# 
# d = 30
# e = 40
# f = d + e

# def add(a, b):
#     """
#     This function add 2 number.
#     """
#     print(a + b)
# 
# add(10, 20)
# add(30, 40)



# Types of paras
#----------------
# positional para

def add(a, b, c):
    """
    This function add 3 number.
    """
    print(a + b + c)

# add(10, 20) # TypeError: add() missing 1 required positional argument: 'c'
# add(10,20,30)


# keyword/default para
# 
# def bill(discount, tomato=20, potato=30):
#     print(tomato + potato)
# 
# bill(5)
# bill(5, tomato=30, potato=50)

# var length para
# *args

# def add(*yoyo):
#     # print(yoyo)
#     print(sum(yoyo))
# #    print(type(yoyo))
# 
# add(10, 20, 30, 40, 50, 50, 10010100110)

# **kwargs

# def bill(discount, **products):
#     # print(products)
#     total_amount = 0
#     for key, value in products.items():
#         print(key, value)
#         total_amount += value
#     print(f"Total amount is : {total_amount}")
#     discount_amount = (5 * total_amount) / 100
#     print(f"total discount is : {discount_amount}")
#     print(f"With discount you need to pay : {total_amount-discount_amount}")
# 
# 
# bill(5, tomato=20, potato=30, onion=50, pen=20, book=40, milk=33, chocolate=7, headphon=800)

# func = lambda x, y: x*y*200
# print(func(10,20))

# nums = [1,2,3,4,5]
# print(list(map(lambda x:x*x, nums)))

# x = 20
# print(id(x))
# def test():
#     global x
#     x = 10
#     print(id(x))
#     print(x, 'inside')
# 
# test()
# print(x, 'outside')

def lower_case(func):
    def wrapper():
        result = func().lower()
        print(f"String is {result}")
        return result
    return wrapper

def length(func):
    def wrapper():
        result = len(func())
        print(f"Length of string is : {result}")
    return wrapper

@length
@lower_case
def takeInput():
    return input("Enter something...  ")

takeInput()
