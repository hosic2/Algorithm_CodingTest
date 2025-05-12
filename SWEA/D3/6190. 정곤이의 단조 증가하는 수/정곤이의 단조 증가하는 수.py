t = int(input())

for x in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    answer = -1

    for i in range(n):
        for j in range(i + 1, n):
            num = arr[i] * arr[j]
            s = str(num)
            flag = True

            for k in range(1, len(s)):
                if s[k] < s[k - 1]:
                    flag = False
                    break

            if flag and num > answer:
                answer = num

    print(f'#{x}', answer)
