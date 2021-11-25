def perm(lst):
    if len(lst) == 1:
        return [lst]
    vysledek = []
    for i in range(len(lst)):
        zbytek = lst[:i] + lst[i+1:]
        perm_zbytku = perm(zbytek)
        for p in perm_zbytku:
            vysledek.append([lst[i],*p])
    return vysledek

print(perm([1,2,3]))
            
