# Největší společný dělitel: Euklidův algoritmus s odčítáním

x = int(input())
y = int(input())

while x > 0 and y > 0:
    if x > y:
        x %= y
    else:
        y %= x

if x > 0:
    print(x)
else:
    print(y)
