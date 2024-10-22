m, n = map(int, input().split())
answer = [i for i in range(1, m+1)]

for x in range(n):
    i, j = map(int, input().split())
    answer[i - 1], answer[j - 1] = answer[j - 1], answer[i - 1]

for i in range(m):
    print(answer[i], end=' ')