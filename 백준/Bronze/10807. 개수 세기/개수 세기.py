n = int(input())
num = list(map(int, input().split()))
f = int(input())
count = 0
for i in num:
    if i == f:
        count += 1
print(count)