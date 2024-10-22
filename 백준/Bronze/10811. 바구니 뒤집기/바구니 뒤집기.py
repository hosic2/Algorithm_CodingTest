m, n = map(int, input().split())
numlist = [i for i in range(1, m + 1)]

for x in range(n):
    i, j = map(int, input().split())
    numlist[i - 1:j] = numlist[i - 1: j:][::-1]

for i in range(m):
    print(numlist[i], end=' ')