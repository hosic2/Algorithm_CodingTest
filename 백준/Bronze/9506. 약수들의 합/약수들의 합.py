while True:
    n = int(input())

    if n == -1:
        break
    
    temp = []

    for i in range(1, n):
        if n % i == 0:
            temp.append(i)

    if n == sum(temp):
        print(n, '=', ' + '.join(str(i) for i in temp))
    else:
        print(n, 'is NOT perfect.')