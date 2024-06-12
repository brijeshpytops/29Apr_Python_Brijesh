# class Math:
#     def calc(self, a, b):
#         print(a + b)

#     def calc(self, a, b, c):
#         print(a * b * c)

# obj =  Math()
# obj.calc(10, 20, 30)
# obj.calc(10, 20)

# class Math:
#     def calc(self, a=None, b=None, c=None):
#         if (a!=None and b!=None and c!=None):
#             print(a + b + c)
#         elif (a!=None and b!=None):
#             print(a + b)

# obj =  Math()
# obj.calc(10, 20)

# class Math:
#     def sum(self, a, b):
#         print("I am from base class")
#         print(a+b)

# class Math1(Math):

#     def sum(self, a, b):
          # Call the parent class's sum method
#         # super().sum(230, 40)
          # Directly call the parent class's sum method
          # Math.sum(self, a, b)
#         print("I am from child class")
#         print(a+b)


# obj = Math1()
# obj.sum(10, 20)