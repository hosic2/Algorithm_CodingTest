n, m, l = map(int, input().split())

arr = [1] + [0] * (n - 1)
start = 0
cnt = 0

while True:
    if arr[start] == m:
        print(cnt)
        break

    if arr[start] % 2 == 0:
        start = abs((start - l) % n)
        arr[start] += 1
        cnt += 1
    else:
        start = (start + l) % n
        arr[start] += 1
        cnt += 1