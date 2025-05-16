t = int(input())
for i in range(1, t + 1):
    l = sorted(list(map(int, input().split())))
    print(f'#{i}', round(sum(l[1:-1]) / (len(l) - 2)))