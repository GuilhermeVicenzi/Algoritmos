from random import randint

s = 0

for i in range(10):
    n1 = randint(0, 10)
    s += n1

print(f"A média é {s}")