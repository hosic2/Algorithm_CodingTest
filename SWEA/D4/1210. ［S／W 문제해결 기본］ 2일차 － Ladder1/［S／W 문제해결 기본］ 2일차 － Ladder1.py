for _ in range(10):
    t = input()

    arr = [list(map(int, input().split())) for _ in range(100)]

    # 아래, 오른쪽, 왼쪽
    dr = [1, 0, 0]
    dc = [0, 1, -1]
    answer = 0

    # 첫 행 길이만큼 반복
    for i in range(100):
        if arr[0][i]:
            r, c = 0, i

            move = 0

            # 행 끝까지 도달하면 도착 못한거니까 종료
            while r < 99:
                if move == 0:
                    # 왼쪽 검사
                    if c > 0 and arr[r][c - 1]:
                        move = 2
                    # 오른쪽 검사
                    elif c < 99 and arr[r][c + 1]:
                        move = 1
                else:
                    if arr[r + 1][c]:
                        move = 0

                r += dr[move]
                c += dc[move]

            if arr[r][c] == 2:
                answer = i
                break

    print(f'#{t}', answer)