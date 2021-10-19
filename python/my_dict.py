""" Dictionary """

this_dict = {
    "name": "Shahriar",
    "age": 25,
    "education": "CSE",
    "job": "Jr. Software Engineer"
}

print(this_dict)
print(len(this_dict))

print(this_dict['name'])
print(this_dict.get('name'))

keys = this_dict.keys()
print(keys)

values = this_dict.values()
print(values)

this_dict['name'] = 'Salpin'
print(this_dict)

items = this_dict.items()
print(items)

if 'namee' in this_dict:
    print(this_dict['namee'])

this_dict.update({'name': 'Shahriar Hosen'})
print(this_dict)


this_dict.pop('name')
print(this_dict)

this_dict.popitem()
print(this_dict)

del this_dict['age']
print(this_dict)

# this_dict.clear()
# print(this_dict)

for i in this_dict:
    print(this_dict[i])

for i, j in this_dict.items():
    print('i ' + i, 'j ' + j)