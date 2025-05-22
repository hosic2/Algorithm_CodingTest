import sys
input = sys.stdin.readline

n = int(input())
l = sorted(list(map(int, input().split())))

while len(l) != 1:
    l[-1] += l.pop(0) / 2

print(int(l[0]) if int(l[0]) == l[0] else l[0])