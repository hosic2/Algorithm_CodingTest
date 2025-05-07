T = int(input())

for t in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]

    dx = [0, 1, 0, -1]  # 우, 하, 좌, 상
    dy = [1, 0, -1, 0]
    x, y, d = 0, 0, 0  # 시작 좌표와 방향 인덱스

    for num in range(1, N * N + 1):
        arr[x][y] = num
        nx = x + dx[d]
        ny = y + dy[d]

        # 범위 밖이거나 이미 채운 칸이면 방향 전환
        if nx < 0 or nx >= N or ny < 0 or ny >= N or arr[nx][ny] != 0:
            d = (d + 1) % 4
            nx = x + dx[d]
            ny = y + dy[d]

        x, y = nx, ny

    # 출력
    print(f'#{t}')
    for row in arr:
        print(' '.join(map(str, row)))