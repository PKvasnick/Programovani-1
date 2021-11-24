#!/usr/bin/env python3
# Binární vyhledávání v setříděném seznamu

def binary_search(kde, co):
    # Hledané číslo se nachazí v intervalu [l, p]
    l = 0
    p = len(kde) - 1

    while l <= p:
        stred = (l + p) // 2
        if kde[stred] == co:  # Našli jsme
            return stred
        elif kde[stred] < co:
            l = stred + 1  # Jdeme doprava
        else:
            p = stred - 1  # Jdeme doleva
    else:
        return -1


def main() -> None:
    """
    :rtype: None
    """
    # Binární vyhledávání v setříděném seznamu
    kde = [11, 22, 33, 44, 55, 66, 77, 88]
    co = int(input())
    result = binary_search(kde, co)
    print(result)


if __name__ == '__main__':
    main()
