# for ch in "Python":
#     print(ch.upper())

# nums = [1,2,3,4,5]
# for num in nums:
#     print(num * num * num)

# for num in range(1,11):
#     print(num)
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# num = 5
# for row in range(1, num+1):
#     for col in range(1, num+1):
#         print("* ", end='')
#     print()


# *
# * *
# * * *
# * * * *
# * * * * *

# num = 5
# for row in range(1, num+1):
#     for col in range(1, row+1):
#         print("* ", end='')
#     print()

# * * * * *
# * * * *
# * * *
# * *
# *

# num = 5
# for row in range(1, num+1):
#     for col in range(1, num+2-row):
#         print("* ", end='')
#     print()


#         *
#       * *
#     * * *
#   * * * *
# * * * * *

# num = 5
# for row in range(1, num+1):
#     for col in range(1, num+1-row):
#         print("  ", end='')
#     for col in range(1, row+1):
#         print("* ", end='')
#     print()


# * * * * *
#   * * * *
#     * * *
#       * *
#         *

# num = 5
# for row in range(1, num+1):
#     for col in range(1, row):
#         print("  ", end='')
#     for col in range(1, num+2-row):
#         print("* ", end='')
#     print()

#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *

# num = 5
# for row in range(1, num+1):
#     for col in range(1, num+1-row):
#         print("  ", end='')
#     for col in range(1, row+1):
#         print("* ", end='')
#     for col in range(1, row):
#         print("* ", end='')
#     print()


# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * * * * * *
#   * * * * * * *
#     * * * * *
#       * * *
#         *

# num = 5
# for row in range(1, num):
#     for col in range(1, num+1-row):
#         print("  ", end='')
#     for col in range(1, row+1):
#         print("* ", end='')
#     for col in range(1, row):
#         print("* ", end='')
#     print()
# for row in range(1, num+1):
#     for col in range(1, row):
#         print("  ", end='')
#     for col in range(1, num+2-row):
#         print("* ", end='')
#     for col in range(1, num+1-row):
#         print("* ", end='')
#     print()
# 


# 
# num = 10
# for row in range(1, num+1):
#     print("* "*(num-row-1))