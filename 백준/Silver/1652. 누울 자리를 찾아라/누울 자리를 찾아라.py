n = int(input())
g = [input().strip() for _ in range(n)]

def count(s): return sum(len(x) >= 2 for x in ''.join(s).split('X'))

print(sum(count(r) for r in g), sum(count(c) for c in zip(*g)))