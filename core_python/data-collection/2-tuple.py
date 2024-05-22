"""
Tuple - immutable, ordered, duplicate values are allowed, indexing, slicing

In Python, a tuple is an immutable, ordered collection of elements. Tuples are similar to lists, but unlike lists, tuples cannot be changed after their creation (they are immutable). They can hold a sequence of elements of any type, including other tuples. 

Immutable: Once a tuple is created, you cannot modify its contents. This means you cannot add, remove, or change elements in a tuple.

Ordered: The elements in a tuple have a defined order, and that order will not change.

Heterogeneous: Tuples can contain elements of different types, including integers, strings, lists, other tuples, etc.

Indexing and Slicing: You can access elements of a tuple by indexing and can obtain a range of elements by slicing, similar to lists.

Parentheses: Tuples are defined using parentheses () with elements separated by commas.

syntax :

tuple_name = ()
tuple_name = tuple()
comma_tuple_name = 1,
comma_tuple_name = 1,2,3
"""

nums = (1,2,3,4,5,1,1,1)
# 
# nums[0] = 5 # TypeError: 'tuple' object does not support item assignment
# print(nums)

# print(type(nums))
# print(len(nums))

# print(dir(nums))
#  'count', 'index'

# print(nums.count(1))
# print(nums.index(1, 3))


