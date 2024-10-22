total = 0
sum = 0
avg_board = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0': 2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
for i in range(20):
    temp = input().split()
    n, s = float(temp[1]), avg_board.get(temp[2])

    if temp[2] != 'P':
        sum += n
        total += n * s

print(round(total / sum, 6))