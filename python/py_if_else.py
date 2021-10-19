""" Conditional Statements """

a = 33
b = 33

if b > a:
    print("b is greater than a")
elif b >= a:
    print("b is greater than of equal a")
else:
    print("b is less than a")



#  example
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} is even number.")
    else:
        print(f"{i} is odd number.")
