from collections import deque

t = int(input())

for _ in range(t):
    p = input()
    n = int(input())
    arr = input()

    dq = deque() if n == 0 else deque(arr[1:-1].split(','))

    rev = False
    error = False

    for cmd in p:
        if cmd == 'R':
            rev = not rev # 논리적으로만 뒤집기
        elif cmd == 'D':
            if not dq:
                error = True
                break
            if rev:
                dq.pop()
            else:
                dq.popleft()

    if error:
        print('error')
    else:
        if rev:
            dq.reverse()
        print(f"[{','.join(dq)}]")