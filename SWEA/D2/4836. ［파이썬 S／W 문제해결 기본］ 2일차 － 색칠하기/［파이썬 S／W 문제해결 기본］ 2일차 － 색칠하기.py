T = int(input())

for tc in range(T):
    N = int(input())
    grid = [[0] * 10 for _ in range(10)]  # 10x10 격자 초기화

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for r in range(r1, r2 + 1):
            for c in range(c1, c2 + 1):
                if grid[r][c] == 0:
                    grid[r][c] = color
                elif grid[r][c] != color:
                    grid[r][c] = 3  # 보라색

    # 보라색(3)인 칸 수 세기
    count = sum(row.count(3) for row in grid)
    print(f'#{tc + 1}', count)