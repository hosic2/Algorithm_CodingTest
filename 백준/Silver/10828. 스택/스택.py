import sys

T = int(sys.stdin.readline())

l = []

for _ in range(T):
    temp = sys.stdin.readline().split()
    
    if temp[0] == 'push':
        l.append(temp[1])
    elif temp[0] == 'top':
        if not l:
            print(-1)
        else:
            print(l[-1])
    elif temp[0] == 'size':
        print(len(l))
    elif temp[0] == 'pop':
        if not l:
            print(-1)
        else:
            print(l.pop())
    elif temp[0] == 'empty':
        print(1 if not l else 0)