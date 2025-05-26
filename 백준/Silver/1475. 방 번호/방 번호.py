import sys


input = sys.stdin.readline
n = input().strip()
check = [0] * 10

for i in n:
    if i == '6' or i == '9':
        if check[6] <= check[9]:
            check[6] += 1
        else:
            check[9] += 1
    else:
        check[int(i)] += 1

print(max(check))