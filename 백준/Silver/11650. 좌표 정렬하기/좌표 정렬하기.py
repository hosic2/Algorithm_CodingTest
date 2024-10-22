n = int(input())

temp = []

for _ in range(n):
    temp.append(list(map(int, input().split())))

temp.sort(key=lambda x : (x[0], x[1]))

for i in range(n):
    for j in range(len(temp[i])):
        print(temp[i][j], end=' ')
    print()