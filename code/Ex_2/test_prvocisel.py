#!/usr/bin/env python3

# Otestuje, zda číslo je prvočíslem

n = int(input())
d = 2
mam_delitele = False

while d < n:
    if n%d == 0:
        print("Číslo", n, "je dělitelné", d)
        mam_delitele = True
        break
    d += 1

if not mam_delitele:
    print("Číslo", n, "je prvočíslo")
