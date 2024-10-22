exp = list(map(int, input().split()))

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if exp[0] * i + exp[1] * j == exp[2] and exp[3] * i + exp[4] * j == exp[5]:
            print(i, j)
            break