from collections import deque

n, m = map(int, input().split())
targets = list(map(int, input().split()))

dq = deque(range(1, n + 1))
cnt = 0

for t in targets:
    idx = dq.index(t)
    
    if idx <= len(dq) // 2:
        dq.rotate(-idx)
        cnt += idx
    else:
        dq.rotate(len(dq) - idx)
        cnt += len(dq) - idx
    
    dq.popleft()

print(cnt)