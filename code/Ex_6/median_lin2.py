from random import randint


seznam = [randint(1,10) for _ in range(10)]

k = int(input())
print(f"{k=}")

assert(0 <= k - 1 < len(seznam))

low = 0
high = len(seznam)
while high - low > 1 :
    pivot = seznam[randint(low, high - 1)]
    print(f"{low=} {high=} {pivot=} {seznam=}")
    low_numbers = [x for x in seznam[low:high] if x < pivot]
    pivots = [x for x in seznam[low:high] if x == pivot]
    high_numbers = [x for x in seznam[low:high] if x > pivot]
    seznam = seznam[:low] + low_numbers + pivots + high_numbers + seznam[high:]
    mid_low = low + len(low_numbers)
    mid_high = low + len(low_numbers) + len(pivots)
    if k-1 < mid_low:
        high = mid_low
    elif mid_low <= k-1 < mid_high:
        print(seznam)
        print(pivots[0])
        break
    else:
        low = mid_high
else:
    print(seznam)
    print(seznam[low:high][0])


