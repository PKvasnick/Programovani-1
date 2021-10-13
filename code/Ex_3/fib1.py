# Vypsat prvnich n Fibonacciho cisel
n = int(input())
a = 1
print(a, end = ", ")
b = 1
print(b, end = ", ")
for k in range(3,n+1):
    b, a = b+a, b
    print(b, end = ", ")
