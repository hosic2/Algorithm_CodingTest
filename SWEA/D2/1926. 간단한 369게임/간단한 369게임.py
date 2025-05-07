n = int(input())

for i in range(1, n + 1):
    if '3' not in str(i) and '6' not in str(i) and '9' not in str(i):
        print(i, end= ' ')
    else:
        i = str(i)
        for j in i:
            if int(j) % 3 == 0 and int(j) != 0:
                print('-', end='')
        print(end=' ')