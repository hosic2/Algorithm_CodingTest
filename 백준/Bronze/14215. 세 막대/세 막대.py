temp = sorted(list(map(int, input().split())))

if temp[0] + temp[1] > temp[2]:
    print(sum(temp))
else:
    print((temp[0] + temp[1]) * 2 - 1)