# itemgetter as functor

class itemgetter:
    def __init__(self, k):
        self.k = k
        self.fun = lambda a: a[self.k]

    def __call__(self, a):
        return self.fun(a)
    

def main():
    a = (1,2)
    print(itemgetter(1)(a))
    u = [(1,5), (2,4), (3,3)]
    print(sorted(u, key = itemgetter(1)))
    print(sorted(u, key = itemgetter(0)))


if __name__ == "__main__":
    main()
    
