def check():
    cnt = 0

    for i in board:
        if sum(i) == 0:
            cnt += 1
    for i in zip(*board):
        if sum(i) == 0:
            cnt += 1

    if sum(board[i][i] for i in range(5)) == 0:
        cnt += 1

    if sum(board[i][4 - i] for i in range(5)) == 0:
        cnt += 1

    return cnt


board = [list(map(int, input().split())) for _ in range(5)]

cnt = 0
num = 0

for i in range(5):
    temp = list(map(int, input().split()))
    for j in range(5):
        num += 1
        for a in range(5):
            for b in range(5):
                if temp[j] == board[a][b]:
                    board[a][b] = 0

        cnt = check()
        if cnt >= 3:
            print(num)
            exit()