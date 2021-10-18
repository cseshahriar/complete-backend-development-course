""" List Comprehension """

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
print(fruits)

# print(len(fruits))
# for x in fruits:
#     print(fruits.index(x))

new_list = [
    x
    for x in fruits
    if "a" in x
]
print(new_list)