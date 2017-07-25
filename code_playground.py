from random import choices


domain = range(9)
x, y = choices(domain, k=2)
while x != y:
    x, y = choices(domain, k=2)

print(x)
print(y)