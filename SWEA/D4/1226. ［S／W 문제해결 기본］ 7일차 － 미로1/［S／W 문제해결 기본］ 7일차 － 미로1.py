def dfs(x, y):
    global answer
    # 시작점은 방문처리
    arr[x][y] = 1
    # 상 하 좌 우
    dx = [1, -1, 0, 0]
    dy = [0, 0, -1, 1]

    # 상하좌우 모두 체크
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if arr[nx][ny] == 3:
            answer = 1
            return

        if 0 <= nx < 16 and 0 <= ny < 16 and arr[nx][ny] == 0:
            dfs(nx, ny)

for _ in range(10):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    answer = 0

    # 시작점 호출
    dfs(1, 1)

    print(f'#{n}', answer)