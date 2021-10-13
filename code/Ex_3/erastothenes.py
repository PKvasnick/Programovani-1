# vypiš všechna prvočísla menší nebo rovná n

n = int(input())

prvocisla = [True]*(n+1) # včetně nuly a n
prvocisla[0] = False
prvocisla[1] = False
for i in range(2,n+1):
    if prvocisla[i]:
        for j in range(i*i, n+1, i):
            prvocisla[j]=False

print("Pocet: ", sum(prvocisla))
for i in range(n+1):
    if prvocisla[i]:
        print(i, end = ', ')
