import sys

input = sys.stdin.readline
n = int(input().strip())

l = [i for i in range(1, n + 1)]

for i in range(n):
    print(l.pop(0), end=' ')
    if l:
        l.append(l.pop(0))