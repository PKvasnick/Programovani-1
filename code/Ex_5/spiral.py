# Vyplňujeme matici nxn spirálovitě z levého horního rohu doprostředka čísly
# 1,2,...n*n.

n = int(input())

matrix = [[1 for _ in range(n)] for _ in range(n)]  # _ protože proměnné nepotřebujeme

left, right, top, bot = 0, len(matrix[0])-1, 0, len(matrix)-1
i = 1 # číslo, které vyplňujeme

while left <= right and top <= bot: # pokračujeme, dokud je kam vyplňovat
    # Horní řádek zleva doprava
    for col in range(left, right+1):
        matrix[top][col] = i # vyplníme a inkrementujeme
        i += 1
    top += 1 # číslování je shora zleva

    for row in range(top, bot +1):
        matrix[row][right] = i
        i += 1
    right -= 1

    for col in range(right, left-1, -1):
        matrix[bot][col] = i
        i += 1
    bot -= 1

    for row in range(bot, top-1, -1):
        matrix[row][left] = i
        i += 1
    left += 1

for row in range(n):
    for col in range(n):
        print(f'{matrix[row][col]:3}', end = ' ')
    print('\n')
