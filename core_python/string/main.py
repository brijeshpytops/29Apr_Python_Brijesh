# In Python, a string is a sequence of characters enclosed within single quotes ('...'), double quotes ("..."), triple single quotes ('''...'''), or triple double quotes ("""..."""). Strings are one of the most commonly used data types in Python and are immutable, meaning once a string is created, it cannot be changed.

# You can create strings by enclosing characters in quotes:

single_quote_string = 'Hello, World!'
double_quote_string = "Hello, World!"
triple_single_quote_string = '''Hello,
World!'''
triple_double_quote_string = """Hello,
World!"""

# Triple quotes are useful for creating multi-line strings.

"""
Accessing Characters

You can access individual characters in a string using indexing, with the index starting at 0:



"""

code = "python"

# print(type(code))

# print(len(code))

# print(code)


# indexing (+/-)
# --------------
# print(code[0])
# print(code[4])
# print(code[-1])
# print(code[-2])
# print(code[-3])
# print(code[-4])
# print(code[-5])
# print(code[-6])

# slicing (+/-)
# -------------
# print(code[1:4])
# print(code[2:5])
# print(code[1::2])
# print(code[::-1])
# print(code[::-2])


# print(dir(code))

name = 'ToPS TecHoNOlogy PVt. LtD.'

# print(name.lower())
# print(name.upper())
# print(name.title())
# print(name.capitalize())
# print(name.swapcase())


text = "        python code     "
# print(text.lstrip())
# print(text.rstrip())
# print(text.strip())
# print(text.replace(" ", ""))

# print(text.find('code'))
# print(name.lower().count('o'))
# print(name.count('O'))

# center = "python"
# print(center.center(20, '-'))

# password = "132431225"
# password = "132431225a"
# print(password.isdigit())
# password = "132431225a"
# print(password.isalnum())
# print(not password.isalnum())
# 
# password = "BRIJESH"
# print(password.isupper())
# print(not password.isupper())



name = "python"
price = 300.5467554
page = 642

# print("Book name is python, its price is 300.5467554 and its pages is 642")
# print(f"Book name is {name}, its price is {price} and its pages is {page}")
# print("Book name is {}, its price is {} and its pages is {}".format(name, price, page))
# print("Book name is {0}, its price is {2} and its pages is {1}".format(name,  page, price))
# print("Book name is %s, its price is %f and its pages is %d" % (name, price, page))
# print("Book name is %s, its price is %.2f and its pages is %d" % (name, price, page))


"""
Escape SequencesStrings can contain special characters using escape sequences:
\n: Newline
\t: Tab
\\: Backslash
\': Single quote
\": Double quote
"""

# print('my name is "brijesh gondaliya"')
# print("my name is 'brijesh gondaliya'")
# print('my name is \'brijesh gondaliya\'')
# 
# print('\'')
# print('\"')
# print('\\')
# print('\\\\')

# print(r"brijesh go\ndaliya")
# print(r"brijesh go\ndaliya")

# print("* "*5 )

# fname = "brijesh"
# lname = "gondaliya"
# fullname = fname + ' ' + lname 
# print(fullname)

# for ch in "python":
    # print(ch)

for num in range(1, 27):
    print(num, chr(num + 64), '-', ord(chr(num + 64)) , chr(num + 96), '-', ord(chr(num + 96)))