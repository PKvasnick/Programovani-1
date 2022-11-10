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
    low_numbers = [x for x in seznam[low:high] if x <= pivot]
    high_numbers = [x for x in seznam[low:high] if x > pivot]
    seznam = seznam[:low] + low_numbers + high_numbers + seznam[high:]
    mid = low + len(low_numbers)
    if k-1 < mid:
        high = mid
    else:
        low = mid


print(seznam)
print(seznam[low:high][0])


