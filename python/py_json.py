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