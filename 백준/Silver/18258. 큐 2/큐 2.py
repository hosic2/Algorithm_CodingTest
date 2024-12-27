import sys
from collections import deque

input = sys.stdin.read
commands = input().splitlines()
N = int(commands[0])

queue = deque()

for i in range(1, N + 1):
    cmd = commands[i].split()
    if cmd[0] == "push":
        queue.append(cmd[1])
    elif cmd[0] == "pop":
        print(queue.popleft() if queue else -1)
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        print(1 if not queue else 0)
    elif cmd[0] == "front":
        print(queue[0] if queue else -1)
    elif cmd[0] == "back":
        print(queue[-1] if queue else -1)