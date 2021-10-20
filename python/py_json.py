""" json """
import json

# json to dict
x = '{ "name":"John", "age":30, "city":"New York"}'
y = json.loads(x)
print(y, type(y))
print(y["age"])
print(y.get('age'))


# dict to json
m = {
    "Name": "Shahriar",
    "age": 25,
    "edu": "CSE",
    "city": "Dhaka"
}

print(m, type(m))

n = json.dumps(m)
print(n, type(n))


print("\n")
# read from file
with open("person.json") as json_file:
    data = json.load(json_file)

print(data, type(data))


print("\n")
# write to json file
person_dict = {
   "name": "Bob",
   "languages": ["English", "Fench"],
   "married": True,
   "age": 32
}

with open("person2.text", 'w') as json_file:
    json.dump(person_dict, json_file)

with open("person2.text") as json_file:
    data2 = json.load(json_file)

print(data, type(data2))
