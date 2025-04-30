N, M = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
total = 0
left = 0

for right in range(N):
    total += A[right]
    
    while total > M:
        total -= A[left]
        left += 1
    
    if total == M:
        cnt += 1

print(cnt)