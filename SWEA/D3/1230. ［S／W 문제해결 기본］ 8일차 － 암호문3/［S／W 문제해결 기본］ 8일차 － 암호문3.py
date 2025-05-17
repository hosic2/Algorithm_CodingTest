from collections import deque

for t in range(1, 11):
    N = int(input())
    code = list(input().split())
    M = int(input())
    cmd = deque(input().split())

    while cmd:
        op = cmd.popleft()

        if op == 'I':
            x = int(cmd.popleft())
            y = int(cmd.popleft())
            s = [cmd.popleft() for _ in range(y)]
            code[x:x] = s  # 앞에 삽입

        elif op == 'D':
            x = int(cmd.popleft())
            y = int(cmd.popleft())
            del code[x:x+y]

        elif op == 'A':
            y = int(cmd.popleft())
            s = [cmd.popleft() for _ in range(y)]
            code.extend(s)

    print(f'#{t}', *code[:10])