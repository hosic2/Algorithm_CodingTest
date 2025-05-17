T = int(input())

for x in range(1, T + 1):
    v = int(input())
    s = 0
    d = 0
    
    for i in range(v):
        arr = list(map(int, input().split()))
        if arr[0] == 1:
            s += arr[1]
        elif arr[0] == 2:
            if s > arr[1]:
                s -= arr[1]
            else:
                s = 0
        d += s
        
    print(f'#{x}', d)