""" for loop """

for i in range(10, -1, -1):  # start = , stop: 10-1, step=1
    print(i)

fruits = ["Shahriar", 25, "CSE"]
print(len(fruits))

for data in fruits:
    if data == 25:
        break  # stop
    else:
        print(data)

print("\n")
fruits2 = ["apple", "banana", "cherry"]
for index, value in enumerate(fruits2):
    if value == 'banana':
        continue # skip
    print(index, value)


for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} * {j} ", i*j)

    print("\n")