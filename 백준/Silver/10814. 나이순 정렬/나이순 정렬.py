n = int(input())

temp = []

for _ in range(n):
    age, name = input().split()
    temp.append([int(age),name])

for i in sorted(temp, key=lambda x : x[0]):
    print(i[0], i[1])