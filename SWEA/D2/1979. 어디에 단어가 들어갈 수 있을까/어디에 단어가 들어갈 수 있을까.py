t = int(input())

for m in range(1, t + 1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    result = 0

    for i in range(n):
        # 가로 탐색
        temp = 0
        for j in range(n):
            if arr[i][j] == 1:
                temp += 1
            if arr[i][j] == 0 or j == n - 1:
                if temp == k:
                    result += 1
                temp = 0

        # 세로 탐색
        temp = 0
        for j in range(n):
            if arr[j][i] == 1:
                temp += 1
            if arr[j][i] == 0 or j == n - 1:
                if temp == k:
                    result += 1
                temp = 0

    print(f'#{m}', result)