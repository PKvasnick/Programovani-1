# k prvků bez třídění - FRAGMENT, nefunguje samostatně. 
...
n = len(seznam)
for i in range(k): # k nejmenších hodnot
	pmin = i # poloha minima
	for j in range(i+1, n): # hledáme minimum ve zbývající části
		if seznam[j] < seznam[pmin]:
			pmin = j
	x[i], x[pmin] = x[pmin], x[i] # prohodíme s i-tým prvkem
minsum = sum(seznam[:k])
for i in range(n-1,n-k-1,-1):
    pmax = i
    for j in range(i-1,-1,-1):
        if seznam[j] > seznam[pmax]:
            pmax = j
    seznam[j], seznam[pmax] = seznam[pmax], seznam[j]
maxsum = sum(seznam[-k:])
