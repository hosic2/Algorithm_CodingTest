import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

start, end = 1, max(lines)

while start <= end:
    mid = (start + end) // 2
    line_cnt = sum(line // mid for line in lines)

    if line_cnt >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)