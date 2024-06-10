class auth:
    def __init__(self, otp):
        self.otp = otp
    
    class login:
        def __init__(self, email, password):
            self.email =  email
            self.password = password

        def login(self):
            if self.email == 'admin@gmail.com' and self.password == 'admin':
                print("You are logged In")
            else:
                print("Invalid email or password")

    class forgotPassword:
        def __init__(self, email, otp):
            self.__email = email
            self.otp = otp

        def send_mail(self):
            print(f"Please check your {self.email}. ")
            print(f"Your otp is : {self.otp}")

import random
otp = random.randint(1111, 9999)


# objAuth = auth(otp).login('admin@gmail.com', 'admin')
# objAuth.login()

objFP = auth(otp).forgotPassword("admin@gmail.com", otp)
# objFP.send_mail()

# print(objFP.__email)
print(objFP._forgotPassword__email)