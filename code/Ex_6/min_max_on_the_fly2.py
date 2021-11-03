# Průběžné hledání pěti největších a pěti nejmenších čísel
# v posloupnosti

from random import randint
# Místo načítání si seznam vygenerujeme
seznam = [randint(1,100) for _ in range(100)]

k = 5
n_sorts = 0 # Budeme sledovat, kolik setřídění potřebujemeů

low_list = [float("Inf")] * (k+1)
hi_list = [float("-Inf")] * (k+1)

for i in seznam:
    if i < low_list[k-1]:
        low_list[k] = i
        low_list.sort()
        n_sorts += 1
    if i > hi_list[1]:
        hi_list[0] = i
        hi_list.sort()
        n_sorts += 1

print(low_list[:k], hi_list[-k:], n_sorts)
