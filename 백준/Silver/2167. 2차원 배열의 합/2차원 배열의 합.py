import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[0] * (m + 1)]
for _ in range(n):
    row = list(map(int, input().split()))
    arr.append([0] + row)
    
sum_arr= [[0] * (m + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, m + 1):
        sum_arr[i][j] = sum_arr[i - 1][j] + sum_arr[i][j - 1] + arr[i][j] - sum_arr[i - 1][j - 1]

k = int(input())
for m in range(k):
    i, j, x, y = map(int, input().split())
    result = sum_arr[x][y] - sum_arr[i - 1][y] - sum_arr[x][j - 1] + sum_arr[i - 1][j - 1]
    print(result)