""" function """

# definition
def my_print(msg):
    print(msg)


# call
my_print("Hello")

my_print("Welcome")


# sum
def my_sum(num1: int, num2: int = 5):  # parameter
    return num1 + num2


result = my_sum(3, 6)  # argument
print(result)
