m, n = map(int, input().split())

temp = []

for i in range(1, m + 1):
    if m % i == 0:
        temp.append(i)

if len(temp) < n:
    print(0)
else:
    print(temp[n-1])