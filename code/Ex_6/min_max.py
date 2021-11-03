# Vypiš minimální a maximální součet k prvků posloupnosti

seznam = []
while True:
    a = int(input())
    if a == -1:
        break
     else:
        seznam.append(a)
k = int(input())

seznam.sort()
print(seznam[:k], seznam[-k:])
