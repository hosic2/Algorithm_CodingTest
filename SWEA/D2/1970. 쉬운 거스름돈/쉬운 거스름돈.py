T = int(input())

for x in range(1, T + 1):
    n = int(input())
    units = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = []

    for u in units:
        result.append(n // u)
        n %= u

    print(f'#{x}')
    print(*result)