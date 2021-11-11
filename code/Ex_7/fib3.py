# Momoised Fibonacci

def memoize(f):
    values = [0,1]
    fibs = [0,1]
    def inner(n):
        if n in values:
            return fibs[values.index(n)]
        else:
            result = f(n)
            values.append(n)
            fibs.append(result)
            return result
    return inner

@memoize
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

print(fib(100))
