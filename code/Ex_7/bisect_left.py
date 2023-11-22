from random import randint
import sys

data = sorted([randint(1,10) for _ in range(20)])

print(data)

target = int(input("Zadej číslo: "))

left = 0
right = len(data) - 1

if data[left] == target:
    print(f"Hodnota nalezena v poloze {left}")
    sys.exit()
while right - left > 1:
    mid = (left + right) // 2
    val = data[mid]
    if val < target:
        left = mid
    else:
        right = mid

if data[right] != target:
    print(f"Hodnota {target} nenalezena")
else:
    print(f"Hodnota {target} nalezena v poloze {right}")
