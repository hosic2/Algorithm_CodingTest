a = 2000
b = 2000

for i in range(5):
    temp = int(input())
    if i < 3 and a > temp:
        a = temp
    elif i >= 3 and b > temp:
        b = temp

print(a + b - 50)