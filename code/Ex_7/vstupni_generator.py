def read_list():
    while True:
        i = int(input())
        if i == -1:
            break
        yield i
    return 

for i in read_list():
    print(f"Načetlo se číslo {i}.")

print("Konec cyklu 1")

for j in read_list():
    print(f"Teď se načetlo číslo {i}")
    
print("Konec cyklu 2")
    
    
