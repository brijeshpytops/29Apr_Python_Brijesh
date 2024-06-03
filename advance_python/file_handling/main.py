# create file 
# open("example1.txt", 'x')


# write data into the file
# file = open("example.txt", 'w')
# file.write("this is a python programming.")
# file.close()
# file.write("this is a java programming.") # ValueError: I/O operation on closed file.

# file = open("example.txt", 'r')
# print(file.read())
# print(file.read(10))
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readline())
# print(file.readlines())
# file.close()

# lines = ['This is a line - 1\n', 'This is a line - 2\n', 'This is a line - 3\n', 'This is a line - 4\n', 'This is a line - 5\n', 'line-6']

# file = open("example.txt", 'w')
# file.writelines(lines)
# file.close()


# file = open("example.txt", 'w')
# file.seek(5)
# print(file.tell())
# file.write("code")
# print(file.tell())
# file.close()

import os

# os.rename('example1.txt', 'example2.xlsx')

# os.remove('example2.xlsx')

# print(os.curdir)
# print(os.getcwd())

while(1):
    import datetime
    product = input("Enter a product name: ")
    print("create : press 0\nread : press 1\nupdate : press 2\ndelete : press 3 ")
    option = int(input("Choose options:"))
    CRUD = ['create', 'read', 'update', 'delete']



    f = open('log.txt', 'a')
    log_msg = f'{datetime.datetime.now().date()}-{datetime.datetime.now().time()}_{CRUD[option]}_{product}'
    f.write(log_msg + '\n\n')
    f.close()
