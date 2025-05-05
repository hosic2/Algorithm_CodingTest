import sys

input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
prefix_sum = 0
remainder_count = [0] * m

for a in A:
    prefix_sum += a
    remainder = prefix_sum % m
    if remainder == 0:
        cnt += 1
    remainder_count[remainder] += 1

# 나머지가 같은 것들 중 2개를 뽑는 조합의 수
for c in remainder_count:
    if c > 1:
        cnt += c * (c - 1) // 2

print(cnt)