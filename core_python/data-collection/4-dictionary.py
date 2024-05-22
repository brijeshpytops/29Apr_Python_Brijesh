"""
dictionary - mutable, unindexed, duplicate keys are not allowed
a dictionary is an unordered collection of key-value pairs. Each key in a dictionary must be unique, and each key maps to a value. Dictionaries are mutable, meaning you can add, remove, or modify key-value pairs after the dictionary is created. 

syntax : 

dict_name = {
    'key1':'value1',
    'key2':'value2',
    'key3':'value3',
}
"""
contacts = {
    'A':[
        {'ajay':{
            'mobile':['5643216543', '327857635']
        }, 
        'aman':{
            'mobile':['6753266325']
        }}
        ],
    'B':['bubban', 'bunty'],
    'C':['chagan', 'chandu']
}

# print(type(contacts))
# print(len(contacts))

# print(contacts)
# print(contacts['A'])
# print(contacts['A'][0])
# print(contacts['A'][0]['ajay'])
# print(contacts['A'][0]['ajay']['mobile'])
# print(contacts['A'][0]['ajay']['mobile'][1])

# print(dir(contacts))
# '', '', '', '', '', '', '', '', '', 'update', ''
# contacts.clear()
# print(contacts)

products = {
    'tomato':30,
    'potato':25,
    'onion':55
}

# products.pop('potato')
# products.popitem()

print(products)

# print(products.get('tomato'))
# print(products.keys())
# print(len(products.keys()))
# for k in products.keys():
#     print(k)
# for v in products.values():
#     print(v)
# for k, v in products.items():
#     print(k, v)

# items = ['tomato', 'potato', 'onion']
# price = 30
# 
# make_dict = dict()
# print(make_dict.fromkeys(items, price))

car = {
    'name':"BMW",
    # 'color': 'red'
}
car.setdefault('color', 'black')

new_data = {
    'price':"52L",
    'color':'Blue'
}

car.update(new_data)

print(car)

x = 10
x = 20
print(x)