import sys

input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))

# 누적 합 배열
S = [0] * n

# 나머지 값 저장 배열
C = [0] * m
cnt = 0

# 합 배열 공식을 위해 첫번째 합 배열 값 대입
S[0] = A[0]

for i in range(1, n):
    S[i] = S[i-1] + A[i]
    
for i in range(n):
    remainder = S[i] % m
    if remainder == 0:
        cnt += 1
    C[remainder] += 1
    
for i in range(m):
    if C[i] > 1:
        # 조합 공식
        cnt += C[i] * (C[i] - 1) // 2

print(cnt)