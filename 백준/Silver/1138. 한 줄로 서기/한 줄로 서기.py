N = int(input())
l = list(map(int, input().split()))
line = []

for i in range(N, 0, -1):
    count = l[i - 1]
    line.insert(count, i)

print(*line)