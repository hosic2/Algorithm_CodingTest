for i in range(10):
    n = int(input())
    a = list(map(int, input().split()))
    answer = 0

    for j in range(2, n - 2):
        around = [a[j - 2], a[j - 1], a[j + 1], a[j + 2]]
        if a[j] > max(around):
            answer += a[j] - max(around)

    print(f'#{i + 1}', answer)