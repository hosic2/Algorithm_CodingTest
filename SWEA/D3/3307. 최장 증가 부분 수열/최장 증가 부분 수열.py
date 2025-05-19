T = int(input())
for t in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))

    dp = [1] * N
    for i in range(1, N):
        for j in range(i):
            if A[j] <= A[i]:  # 비내림차순이므로 <=
                dp[i] = max(dp[i], dp[j] + 1)

    print(f"#{t} {max(dp)}")