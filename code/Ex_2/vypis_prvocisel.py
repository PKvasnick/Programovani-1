#!/usr/bin/env python3
# Vypíše všechna prvočísla od 1 do n

n = int(input())

x = 2
while x <= n:
    d = 2
    while d < x:
        if x%d == 0:
            break
        d += 1
    else:
        print(x)

    x += 1
