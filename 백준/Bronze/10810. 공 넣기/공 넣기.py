m, n = map(int, input().split())
answer = [0] * m

for i in range(n):
    i, j, k = map(int, input().split())

    for x in range(i - 1, j):
        answer[x] = k

for i in range(m):
    print(answer[i], end=' ')