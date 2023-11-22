data = [1, 1, 2, 2, 2, 3, 4, 4, 5, 5, 5]

index = dict()
for i, val in enumerate(data):
    if val in index.keys():
        pass
    else:
        index[val] = i

target = int(input("Zadej hodnotu: "))
if target in index.keys():
    print(f"Hodnota nalezena na pozici {index[target]}.")
else:
    print("Hodnota nenalezena.")