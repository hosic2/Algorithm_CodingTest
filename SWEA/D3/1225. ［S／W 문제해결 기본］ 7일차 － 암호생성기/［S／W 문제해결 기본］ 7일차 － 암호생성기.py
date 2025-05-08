from collections import deque

for k in range(1, 11):
    t = input()
    arr = deque(map(int, input().split()))
    i = 1
    
    while 0 not in arr:
        temp = arr.popleft() - i
        
        if temp <= 0:
            arr.append(0)
        else:
            arr.append(temp)
        i = i % 5 + 1
        
    print(f'#{t}', *arr)