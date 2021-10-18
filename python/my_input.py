""" Input """
name = input("Please enter your name: ")
print(name, type(name))

# Assignment operators =
num1 = int(input("Num1 "))
num2 = int(input("Num2 "))
num1 + 1
num2 -= 4

# arithmetic operators +, -
add = num1 + num2
sub = num1 - num2

print(add)


# comparison operators
num = 4
if num % 2 == 0:
    print('Event number')
else:
    print('Odd Number')

print(2 == 3)
print(2 < 3)
print(2 > 3)

# logical operator
x = 5
y = 6

if x < 5 and y <= 6:
    print('True')

if x < 5 or y <= 6:
    print('True')