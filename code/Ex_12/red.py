import operator


def red(s, f):
    res = s[0]
    for i in range(1,len(s)):
        res = f(res, s[i])
    return res


print(red(list(range(10)), operator.add))
print(red(list(range(10)), lambda x, y: str(x) + str(y)))
print(red(list(range(10)), max))
