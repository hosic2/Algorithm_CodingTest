from collections import deque

n, k = map(int, input().split())
deq = deque([i for i in range(1, n + 1)])
answer = []

while deq:
    for _ in range(k-1):
        deq.append(deq.popleft())
    answer.append(str(deq.popleft()))

print('<' + ', '.join(answer) + '>')