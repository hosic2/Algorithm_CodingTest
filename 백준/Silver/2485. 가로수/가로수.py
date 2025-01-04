import math

n = int(input())
temp = [int(input()) for _ in range(n)]

distances = [temp[i] - temp[i - 1] for i in range(1, len(temp))]

min_diff = distances[0]
for d in distances[1:]:
    min_diff = math.gcd(min_diff, d)

maxlen = (temp[-1] - temp[0]) // min_diff + 1
print(maxlen - len(temp))