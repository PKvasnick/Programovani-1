# Emulate math.isqrt

n = int(input())

l = 0
p = n

while l < p:
    m = int(0.5 * (l+p))
    print(l, m, p)
    if m*m == n: # konec
        print(f"{n} is a perfect square of {m}")
        break
    elif m*m < n:
        l = m
    else:
        p = m
    if p-l <= 1:
        print(f"{n} is not pefect square, isqrt is {l}")
        break
