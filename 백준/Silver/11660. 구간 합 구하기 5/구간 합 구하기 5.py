import sys

input = sys.stdin.readline

n, m = map(int, input().split())

A, D = [], [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(n):
    A.append(list(map(int, input().split())))

# (1, 1)은 자기 자신이 합 값이니까 제외
for i in range(1, n + 1):
    for j in range(1, n + 1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i-1][j-1]
        
for _ in range(m):
    dot = list(map(int, input().split()))
    print(D[dot[2]][dot[3]] - D[dot[0] - 1][dot[3]] - D[dot[2]][dot[1] - 1] + D[dot[0] - 1][dot[1] -1])