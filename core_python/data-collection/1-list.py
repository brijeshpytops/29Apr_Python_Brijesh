"""
List - mutable, ordered, duplicate values are allowed, indexing, slicing
A list is a versatile and fundamental data structure used to store a collection of items. It's a mutable, ordered sequence of elements, meaning you can change its content, and the order of items is preserved. Lists are defined using square brackets [ ] and commas , to separate elements.

syntax : 

list_name = [ele1, ele2,...,elen]
list_name = list()
"""

products = ['pen', 'book']

# print(type(products)) # <class 'list'>

# print(len(products))

# mummy = ['milk', 'butter-milk', 'potato']
# aunty = ['potato', 'tomato']
# mylist = ['drinks', 'chocolate', 'spra'] * 2
# 
# total_products = mummy + mylist + aunty 
# 
# print(total_products)

nums = [1,2,3,4,5,6,7,8,9,10]

# indexing (+/-)
# print(nums[4])
# print(nums[8])
# print(nums[5])
# print(nums[-3])
# print(nums[-10])

# slicing (+/-)
# print(nums[2:9])
# print(nums[7:10])
# print(nums[::-1])
# print(nums[-2:-5:-1])


# print(dir(products))

items = ['drink']

# add
mummy = ['tomato', 'onion' ,'onion']
# items.append(mummy)
# items.extend(mummy)
# items.insert(0, mummy)


# print(len(items))


# update
items += mummy
# items[1] = 'potato' 


# delete
# print(items)
# items.pop()
# items.remove('tomato')
# items.clear()
# del items[1]


# print(items.count('onion'))
# print(items.index('tomato'))

# new_list = items.copy()
# 
# print(items)
# print(id(items))
# print(new_list)
# print(id(new_list))

# items.reverse()
# items.sort()
# print(items)

# nested = [1,2,[3,4,[5,6,[7,8,9,[10]]]]]
# # print(nested[-1])
# # print(nested[-1][-1])
# # print(nested[-1][-1][2])
# print(nested[-1][-1][2][3])
# print(nested[-1][-1][2][3][0])

# mix_list = [1, 2, 3.4, 5.6, 'dfsdf', 78 + 47j]
# print(mix_list)


# mummy = ['milk', 'butter-milk', 'potato']
# aunty = ['potato', 'tomato']
# mylist = ['drinks', 'chocolate', 'spra'] * 2
# 
# total_products = mummy + mylist + aunty 
# 
# for item in total_products:
#     print(item)