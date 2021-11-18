# Insertion sort
from bisect import insort

def insertion_sort(lst):
    n = len(lst)
    if n == 1:
        return lst
    for i in range(1,n):
        free = lst.pop(i)
        insort(lst, free, 0, i)

    return lst

print(insertion_sort([3,2,4,1,1]))
