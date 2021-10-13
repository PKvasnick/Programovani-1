# Vypsat prvnich n Fibonacciho cisel
n = int(input())
fibs = [0]*n
fibs[0] = 1
fibs[1] = 1
for i in range(2,n):
    fibs[i] = fibs[i-1] + fibs[i-2]
print(fibs)
