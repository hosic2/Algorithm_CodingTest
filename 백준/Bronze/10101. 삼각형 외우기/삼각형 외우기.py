temp = {}
sum = 0
for _ in range(3):
    n = int(input())
    if n in temp:
        temp[n] += 1
    else:
        temp[n] = 1
    sum += n

max_value = max(temp.values())

if sum != 180:
    print('Error')
elif max_value == 3:
    print('Equilateral')
elif max_value == 2:
    print('Isosceles')
elif max_value == 1:
    print('Scalene')