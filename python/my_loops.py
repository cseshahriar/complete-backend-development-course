""" Loop """
i = 1  # start

while i <= 6:  # stop
    print(i)
    i += 2  # step


print("\n")
j = 6  # start

while j >= 1:  # stop
    print(j)
    j -= 1  # step


print("\n")
# break
m = 1
while m <= 6:
    print(m)
    m += 1

    if m == 3:
        break  #  stop

print("\n")
# continue
n = 1
while n <= 6:
    n += 1
    if n == 3:
        continue  # skip
    print(n)
