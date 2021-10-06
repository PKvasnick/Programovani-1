#!/usr/bin/env python3
# Největší společný dělitel: Euklidův algoritmus s pár triky navíc

x = int(input())
y = int(input())

while y > 0:
    x, y = y, x%y

print(x)
