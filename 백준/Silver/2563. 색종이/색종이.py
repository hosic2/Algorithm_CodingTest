board = [[0] * 100 for _ in range(100)]  

for _ in range(int(input())):
    x, y = map(int, input().split())

    for i in range(x, x+10):
        for j in range(y, y+10):
            board[i][j] = 1

result = 0 

for i in range(100):
    result += board[i].count(1)

print(result)