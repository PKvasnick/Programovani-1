# Průběžné hledání pěti největších a pěti nejmenších čísel
# v posloupnosti

from random import randint
# Místo načítání si seznam vygenerujeme
seznam = [randint(1,100) for _ in range(100)]

k = 5

low_list = [float("Inf")] * (k+1)
hi_list = [float("-Inf")] * (k+1)

for i in seznam:
    low_list[k] = i
    low_list.sort() # Podle potřeby později nahradíme
    hi_list[0] = i
    hi_list.sort()

print(low_list[:k], hi_list[-k:])
