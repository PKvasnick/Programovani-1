#!/usr/bin/env python3
# Největší společný dělitel: Euklidův algoritmus s modulem

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
