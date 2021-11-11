# Dekorátor, počítající počet volání funkce
def counted(f):
    def inner(n):
        inner.calls += 1
        return f(n)
    inner.calls = 0
    return(inner)

@counted
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

@counted
def fib2(n):
    if n < 2:
        return n
    else:
        f, fp = 1, 0
        for i in range(1,n):
            f, fp = f+fp, f
        return f

for i in range(30):
    fib.calls = 0
    fib2.calls = 0
    print(i, fib(i), fib.calls, fib2(i), fib2.calls)
