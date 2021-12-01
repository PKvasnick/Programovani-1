def combinations(a, n):
    if n == 1:
        for x in a:
            yield [x]
    else:
        for i in range(len(a)):
            for x in combinations(a[i+1:], n-1):
                yield [a[i], *x]
    return 

for p in combinations([1,2,3,4,5],2):
    print(p)
