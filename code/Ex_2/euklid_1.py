#!/usr/bin/env python3
# Největší společný dělitel: Euklidův algoritmus s odčítáním

x = int(input())
y = int(input())

while x != y:
    if x > y:
        x -= y
    else:
        y -= x

print(x)
