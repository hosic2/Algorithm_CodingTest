f, m = map(int, input().split())
c = int(input())
n = int(input())
answer = 0
for i in range(n, 101):
    if f * i + m > c * i:
        answer = 0
        break
    else:
        answer = 1

print(answer)