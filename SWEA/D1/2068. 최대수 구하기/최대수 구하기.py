t = int(input())

for i in range(1, t + 1):
    print(f'#{i}', max(list(map(int, input().split()))))