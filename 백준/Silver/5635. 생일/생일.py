import sys

input = sys.stdin.readline
n = int(input().strip())
l = [list(input().split()) for _ in range(n)]

l.sort(key= lambda x: (int(x[3]), int(x[2]), int(x[1])), reverse=True)

print(l[0][0], l[-1][0], sep='\n', end='')