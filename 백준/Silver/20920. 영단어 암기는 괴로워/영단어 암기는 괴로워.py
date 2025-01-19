import sys
input = sys.stdin.readline

n, m = map(int, input().split())
words = {}

for _ in range(n):
    s = input().strip()
    if len(s) >= m:
        words[s] = words.get(s, 0) + 1

for i in sorted(words.items(), key=lambda x: (-x[1], -len(x[0]), x[0])):
    print(i[0])