t = int(input())

for x in range(1, t + 1):
    n, m, k = map(int, input().split()) 
    s = list(map(int, input().split()))
    
    s.sort()
    flag = True
    for i in range(n):
        time = s[i]
        cnt = (time // m) * k
        
        if cnt < i + 1:
            flag = False
            break
    print(f'#{x}', 'Possible' if flag else 'Impossible')