t = int(input())

for i in range(1, t + 1):
    n = int(input())
    num = [j for j in range(2, n + 1)]
    answer = 1
    print(f'#{i}', 1 - sum(num[::2]) + sum(num[1::2]))