def fn(x: float) -> float:
    return 2**x + x - 11


def eqn_solve(f, l, p, eps=1.0e-12):
    if f(l) > 0 or f(p) < 0:
        print("Hodnoty l a p musí ohraničovat jediný kořen funkce f")
        return None
    while abs(p-l) > eps:
        med = (p+l)/2
        if f(med) < 0:
            l = med
        else:
            p = med
    return med


result = eqn_solve(fn, 1, 4)
print(result, fn(result))