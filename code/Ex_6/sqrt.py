# Najděte přibližnou hodnotu druhé odmocniny x

x = int(input())

l = 0
p = x # Velkorysé počáteční meze

while l < p:
    m = 0.5 * (l+p)
    # print(l, m, p)
    if m*m == x: # konec
        print(f"{x} is a perfect square of {m}") # format string
        break
    elif m*m < x:
        l = m
    else:
        p = m
    if p-l <= 1.0e-6:
        print(f"Square root of {x} is approximately {m}")
        break
