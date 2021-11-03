# Insert a new value into a sorted list

from random import randint
# Generujeme setříděný seznam
seznam = [randint(1,100) for _ in range(100)]
seznam.sort()

hodnota = 55
p_vlozeni = None

if hodnota < seznam[0]:
    p_vlozeni = 0

elif hodnota >= seznam[-1]:
    p_vlozeni = len(seznam)

else:
    l = 0
    p = len(seznam) - 1
    # Z předchozího seznam]l]<=hodnota<seznam[p]
    while p - l > 0:
        m = (p+l)//2
        print(l, m, p)
        if l == m:
            break
        if seznam[m] > hodnota:
            p = m
        elif seznam[m] <= hodnota:
            l = m
    p_vlozeni = p

print(p_vlozeni)

seznam.insert(p_vlozeni, hodnota)
print(seznam)
