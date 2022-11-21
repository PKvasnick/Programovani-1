from random import randint

seznam = [randint(1,100) for _ in range(10)]
print(seznam)
n = len(seznam)

for i in range(n):
    n_vymen = 0
    for j in range(n-1):
        if seznam[j] > seznam[j+1]:
            seznam[j], seznam[j+1] = seznam[j+1], seznam[j]
            n_vymen += 1
    if n_vymen == 0:
        break

print(seznam)
                              
