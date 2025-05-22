import sys
input = sys.stdin.readline

N = int(input())
stair = [int(input()) for _ in range(N)]
dp = [0] * N

for i in range(0, N):
    if i == 0:
        dp[0] = stair[0]
    elif i == 1:
        dp[1] = stair[1] + stair[0]
    else:
        dp[i] = max(stair[i] + stair[i-1] + dp[i-3], stair[i] + dp[i-2])

print(dp[N - 1])