a = []

for _ in range(9):
    a.append(list(map(int, input().split())))

max = 0
max_col, max_row = 0, 0

for i in range(9):
    for j in range(9):
        if max <= a[i][j]:
            max_row = i + 1
            max_col = j + 1
            max = a[i][j]

print(max)
print(max_row, max_col)