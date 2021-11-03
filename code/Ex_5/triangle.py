# Triangle

n = int(input())

row = 1 # length of row "row" is row.
number = 1 # first goes to row 1
triangle = []
triangle.append([]) # row 0, for convenience

for row in range(1,n+1): # 1..n
    triangle.append([])
    for _ in range(1,row+1): # 1..row
        triangle[row].append(number)
        number += 1

triangle.remove([]) # remove row 0
print(triangle)
