n = int(input())

answer = [[0]*4 for _ in range(n)]

for i in range(n):
    a = int(input())

    if a >= 25:
        answer[i][0] = a // 25
        a %= 25
    if a >= 10:
        answer[i][1] = a // 10
        a %= 10
    if a >= 5:
        answer[i][2] = a // 5
        a %= 5
    if a >= 1:
        answer[i][3] = a // 1
        a %= 1

for i in range(n):
    for j in range(len(answer[i])):
        print(answer[i][j], end=' ')
    print()