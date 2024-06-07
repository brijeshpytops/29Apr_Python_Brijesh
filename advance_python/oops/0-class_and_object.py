# class bike:    
#     # Data member (attributes)
#     name = "ktm"
#     price = "1.5L"
#     color = "Orange"

#     # member functions (method)
#     def break_(yoyo):
#         print("break")

#     def horn_(yoyo):
#         print("Horn")

# obj = bike() # object

# print(obj.name)
# print(obj.price)
# print(obj.color)
# obj.break_()
# obj.horn_()


class Register:
    # Constructor
    def __init__(self, username, email, password, confirm_password):
        self.username = username
        self.email = email
        self.password = password
        self.confirm_password = confirm_password

    def check_email(self):
        # Check if the email contains both '@' and '.'
        if '@' not in self.email or '.' not in self.email:
            print("Invalid Email.")
            return False
        else:
            print("Email is correct.")
            return True

    def success_message(self):
        # Validate email
        if not self.check_email():
            return "Please provide a valid email address."
        
        # Check if password and confirm password match
        if self.password != self.confirm_password:
            return "Password and confirm password do not match."
        
        return f"Hello {self.username}, Your registration has been successfully done."

# Example usage
b = Register("brijesh07", "brijesh.gondaliya07@gmail.com", "1234", "1234")
print(b.success_message())
