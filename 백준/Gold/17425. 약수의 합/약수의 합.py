import sys
input = sys.stdin.readline
write = sys.stdout.write

MAX = 1_000_000
dp = [0] * (MAX + 1)
s = [0] * (MAX + 1)

for i in range(1, MAX + 1):
    for j in range(i, MAX + 1, i):
        dp[j] += i
    s[i] = s[i - 1] + dp[i]

t = int(input())
for _ in range(t):
    a = int(input())
    write(f"{s[a]}\n")