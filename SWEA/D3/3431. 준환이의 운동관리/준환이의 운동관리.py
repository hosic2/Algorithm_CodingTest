t = int(input())

for i in range(1, t + 1):
    l, u, x = map(int, input().split())
    
    if x < l:
        print(f'#{i}', l - x)
    elif x > u:
        print(f'#{i}', -1)
    else:
        print(f'#{i}', 0)