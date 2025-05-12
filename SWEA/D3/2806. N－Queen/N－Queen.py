def dfs(row):
    global count
    if row == N:
        count += 1
        return
    for col in range(N):
        if col in cols or (row + col) in diag1 or (row - col) in diag2:
            continue
        cols.add(col)
        diag1.add(row + col)
        diag2.add(row - col)
        dfs(row + 1)
        cols.remove(col)
        diag1.remove(row + col)
        diag2.remove(row - col)

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    count = 0
    cols = set()   # 열 차지 여부
    diag1 = set()  # 오른쪽 대각선 (row + col)
    diag2 = set()  # 왼쪽 대각선 (row - col)
    dfs(0)
    print(f"#{test_case} {count}")
