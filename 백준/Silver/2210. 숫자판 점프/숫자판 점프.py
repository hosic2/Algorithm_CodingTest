def dfs(x, y, string):
    if len(string) == 6:
        result.add(string)
        return

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 5 and 0 <= ny < 5:
            dfs(nx, ny, string + board[nx][ny])


board = [list(input().split()) for _ in range(5)]
result = set()

for i in range(5):
    for j in range(5):
        dfs(i, j, board[i][j])

print(len(result))