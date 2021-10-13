# Vypsat prvnich n Fibonacciho cisel
n = int(input())
fibs = [1,1]
while len(fibs)<n:
	fibs.append(fibs[-1] + fibs[-2])
print(fibs)
