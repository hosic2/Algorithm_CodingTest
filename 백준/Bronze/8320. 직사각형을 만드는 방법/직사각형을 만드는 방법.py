n = int(input())

answer = 0

for i in range(1, n + 1):
    j = i
    while i * j <= n:
        answer += 1
        j += 1

print(answer)