seznam = [
    [1,2],
    [2,3,4],
    [4,5,6,7],
    [7,8,9],
    [9,10]
    ]

seznam.sort(key = len)
print(seznam)

print(max(seznam, key = len))

print(max(seznam, key = sum))

 
    
