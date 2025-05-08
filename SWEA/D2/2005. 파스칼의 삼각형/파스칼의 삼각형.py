t = int(input())

for k in range(1, t + 1):
    n = int(input())

    print(f'#{k}')
    for i in range(n):
        val = 1
        row = [1]
        for j in range(1, i + 1):
            val = val * (i - j + 1) // j
            row.append(val)
        print(*row)
