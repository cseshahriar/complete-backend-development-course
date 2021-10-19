""" Set"""
my_set = {'apple', 'banana', 'cherry', 'apple'}
print(my_set)

print(len(my_set))

my_set.add("Orange")

my_set.update({'papaya'})

my_set.remove('apple')
my_set.discard('banana')

my_set.pop()

my_set.copy()

for x in my_set:
    print(x)

