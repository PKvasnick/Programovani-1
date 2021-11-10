# Fibonacci non-recursive

def fib(n):
    if n < 2:
        return n
    else:
        fpp = 0
        fp = 1
        for i in range(1,n):
            fp, fpp = fp + fpp, fp

    return fp

print(fib(35))
