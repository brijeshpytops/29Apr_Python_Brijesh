# single inheritance

# class A:
#     def a(self):
#         print("I am from class A")
    
# class B(A):
#     def b(self):
#         print("I am from class B")

# obj = B()
# # print(dir(obj))
# obj.a()
# obj.b()

# multilevel inheritance
# class A:
#     def a(self):
#         print("I am from class A")
    
# class B(A):
#     def b(self):
#         print("I am from class B")
# class C(B):
#     def c(self):
#         print("I am from class C")

# # obj = C()
# # print(dir(obj))
# # obj.a()
# # obj.b()
# # obj.c()
    

# multiple inheritance
# class A:
#     def a(self):
#         print("I am from class A")
    
# class B:
#     def b(self):
#         print("I am from class B")
# class C(A,B):
#     def c(self):
#         print("I am from class C")

# obj = C()
# print(dir(obj))
# obj.a()
# obj.b()
# obj.c()
    
# herarchical inh.
class Dadasfather:
    def dadasfather(self):
        print("Dadasfather")

class Dada1(Dadasfather):
    def dada1(self):
        print("Dada1")

class papa1(Dada1):
    def papa1(self):
        print("papa1")
        
class Child1(papa1):
    def child1(self):
        print("Child1")

class papa2(Dada1):
    def papa2(self):
        print("papa2")

class Dada2(Dadasfather):
    def dada2(self):
        print("Dada2")

obj = Child1()
# print(dir(obj))
print(Child1.__mro__)
print(Child1.mro())