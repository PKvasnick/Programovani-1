#!/usr/bin/env python3

# Otestuje, zda číslo je prvočíslem (2. pokus)

n = int(input())
d = 2

while d < n:
    if n%d == 0:
        print("Číslo", n, "je dělitelné", d)
        break
    d += 1
else:
    print("Číslo", n, "je prvočíslo")
