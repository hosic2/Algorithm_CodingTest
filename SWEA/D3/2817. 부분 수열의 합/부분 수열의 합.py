from itertools import combinations

t = int(input())

for x in range(1, t + 1):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    count = 0

    for i in range(1, n + 1):
        for j in combinations(a, i):
            if sum(j) == k:
                count += 1

    print(f'#{x}', count)