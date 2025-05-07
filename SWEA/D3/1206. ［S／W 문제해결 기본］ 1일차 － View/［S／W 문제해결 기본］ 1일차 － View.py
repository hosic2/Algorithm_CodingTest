for i in range(10):
    n = int(input())
    a = list(map(int, input().split()))
    answer = 0

    for j in range(2, len(a) - 2):
        if a[j] > a[j - 1] and a[j] > a[j + 1] and a[j] > a[j - 2] and a[j] > a[j + 2]:
            answer += a[j] - max(a[j + 1], a[j - 1], a[j + 2], a[j - 2])

    print(f'#{i + 1}', answer)