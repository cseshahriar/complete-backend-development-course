""" Lambda """
x = lambda a: a + 10
print(x(5))

y = lambda a, b: a * b
print(y(5, 6))

# root
lst = list(map(lambda x: x ** 2, range(1,5)))
print(lst)