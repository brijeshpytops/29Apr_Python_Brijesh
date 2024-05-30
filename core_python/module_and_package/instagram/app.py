# from auth.register  import  *   

from auth.register import user_register, otp

from auth.login import *
from auth.forgot_password import *

from posts import post
from posts import like
from posts import comment

# import register
# import login
# import forgot_password

print(user_register())
print(otp())
print(user_login())
print(user_forgot_password())

print(post.user_post())
print(like.user_like())
print(comment.user_comment())