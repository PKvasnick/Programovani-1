from random import randint
from bisect import bisect

seznam1 = [randint(1,20) for i in range(10)]
seznam1.sort()
seznam2 = [randint(1,20) for i in range(10)]
seznam2.sort()
print(seznam1)
print(seznam2)

def merge_sorted(list1, list2):
    pinsert = 0
    for l2 in list2:
        pinsert = bisect(list1, l2, pinsert, len(list1))
        list1.insert(pinsert, l2)
        print(l2, pinsert, len(list1)-pinsert)
    return list1.copy()

print(merge_sorted(seznam1, seznam2))
