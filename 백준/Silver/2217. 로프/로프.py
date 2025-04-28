N = int(input())
rope = []

for _ in range(N):
    rope.append(int(input()))
    
rope.sort()

weight = []

for i in rope:
    weight.append(i * N)
    N -= 1

print(max(weight))