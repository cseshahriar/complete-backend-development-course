""" List """
fruits = ["Apple", "Banana", "Cherry"]
#           0        1         2
print(fruits, type(fruits))

# print(dir(fruits))

print(fruits[0])

numbers = [
    [1, 2,  3,  4], # row 0
    #00  01  02  03
    [5, 6, 7, 8] # row 1
    #10  11 12  13
]

print(numbers[1][2])


simple_list = [1,2]
print(simple_list)

simple_list.append(3)
print(simple_list)

simple_list.remove(3)
print(simple_list)

print(len(simple_list))

my_list2 = list((1,4))

print(my_list2)