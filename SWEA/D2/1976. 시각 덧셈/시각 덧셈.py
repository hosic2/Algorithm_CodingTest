t = int(input())

for x in range(1, t + 1):
    time = list(map(int, input().split()))
    total = time[0] * 60 + time[2] * 60 + time[1] + time[3]
    
    h = (total // 60) % 12
    m = total % 60
    
    print(f'#{x}', 12 if h == 0 else h, m)