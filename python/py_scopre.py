"""Scope"""

# local scope
def my_func():
    x = 300  # x is local variable
    y = 4
    print(x)


my_func()


#  global scope
m = 100  # global variable

def my_func2():
    print(m)  # local scope

my_func2()

print(m)
