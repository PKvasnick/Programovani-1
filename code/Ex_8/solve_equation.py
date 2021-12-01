def fun(x):
    return 2**x + x - 11

def eqn_solve(f, l, p, eps = 1.0e-6):
    """We expect f(l) < 0 < f(p)"""
    if f(l) > 0 or f(p) < 0:
        print("l a p musí ohraničovat oblast, kde se nachází kořen. ")
        return None
    while abs(l-p) > eps:
        m = (l+p)/2
        if f(m)<0:
            l = m
        else:
            p = m
    return m

def main():
    print(eqn_solve(lambda x: 2**x + x - 20, 0, 4))

main()
    
