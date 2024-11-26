from random import shuffle # pro generování dat


def zeros_back(data: list[int]) -> list[int]:
    left = 0
    right = 0
    n = len(data)
    while left < n:
        if data[left] > 0: # hledáme nulu
            left += 1
            continue
        right = left
        while right < n and data[right] == 0: # hledáme následující nenulovou hodnotu
            right += 1
        if right == n: # od left do konce seznamu jsou samé nuly, končíme.
            break
        data[left], data[right] = data[right], data[left] # Nalezli jsme, vyměníme
        left += 1
    return data


def read_data() -> list[int]:
    data = []
    while (n := int(input())) != -1:
        data.append(n)
    return data


def generate_data() -> list[int]:
    data = [i for i in range(1, 10)] + [0] * 10
    shuffle(data)
    return data


def main() -> None:
    data = generate_data()
    print(data)
    print(zeros_back(data))


if __name__ == '__main__':
    main()