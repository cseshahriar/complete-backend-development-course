""" Tuple """

my_tuple = ('apple', 'banana', 'apple2')
print(my_tuple, type(my_tuple))

# print(dir(my_tuple))

print(len(my_tuple))

print(my_tuple[0])

print(my_tuple[-1])

print(my_tuple[0:3])  # start, stop
print(my_tuple[:2])  # start from > 2
print(my_tuple[2:])  # from start

# add
y = ("Orange",)
my_tuple += y
print(my_tuple)

(var1, var2, *var3) = my_tuple
print(var1, var2, var3)

for item in my_tuple:
    print(item)