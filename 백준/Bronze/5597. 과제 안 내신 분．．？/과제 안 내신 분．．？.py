numlist = [i for i in range(1, 31)]

for i in range(28):
    numlist.remove(int(input()))

for i in numlist:
    print(i)