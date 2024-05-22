"""
Set - always return unique value, Mutable, unordered, duplicate values are not allowed, indexing and sllicing not allowed
A set is an unordered collection of unique elements. Here are some key characteristics of sets:

Unordered: The elements in a set do not have a specific order.
Unique: A set automatically removes duplicate elements, ensuring all elements are unique.
Mutable: You can add or remove elements from a set after its creation.
Defined with Curly Braces: Sets are defined using curly braces {} or the set() function.

syntax:

set_name = {1,2,3,4}
set_name = set()
"""

s = {1,2,3,4,1,1,1,1,1,3,3,4,4,4}
# print(type(s))
# print(s)
# s[2] = 323 # TypeError: 'set' object does not support item assignment

f = frozenset(s) # immutable

# s.add(323)
# print(s)

print(dir(f))
