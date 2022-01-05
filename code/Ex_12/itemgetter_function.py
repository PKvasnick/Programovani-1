# itemgetter as function


def itemgetter(k):
    return lambda a: a[k]
    

def main():
    a = (1,2)
    print(itemgetter(1)(a))
    u = [(1,5), (2,4), (3,3)]
    print(sorted(u, key = itemgetter(1)))
    print(sorted(u, key = itemgetter(0)))


if __name__ == "__main__":
    main()
    
