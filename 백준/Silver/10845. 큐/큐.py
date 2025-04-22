import sys

N = int(input())

l = []

for _ in range(N):
    command = sys.stdin.readline().strip().split()
    
    if command[0] == 'push':
        l.append(command[1])
    elif command[0] == 'pop':
        print(l.pop(0) if l else -1)
    elif command[0] == 'size':
        print(len(l))
    elif command[0] == 'empty':
        print(0 if l else 1)
    elif command[0] == 'front':
        print(l[0] if l else -1)
    elif command[0] == 'back':
        print(l[-1] if l else -1)
