arr = [0]

for _ in range(10):
    arr.append(int(input()))

sum_arr = [0] * 11

for i in range(1, 11):
    sum_arr[i] = sum_arr[i - 1] + arr[i]

answer = 0

for i in sum_arr:
    if abs(i - 100) < abs(answer - 100):
        answer = i
    elif abs(i - 100) == abs(answer - 100) and i > answer:
        answer = i

print(answer)