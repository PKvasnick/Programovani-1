#!/usr/bin/env python3

# Načteme ze vstupu posloupnost čísel, ukončenou -1.
# Vypíšeme jejich součet.

s = 0
while True:
    n = int(input())
    if n == -1:
        break
    s += n
print(s)
