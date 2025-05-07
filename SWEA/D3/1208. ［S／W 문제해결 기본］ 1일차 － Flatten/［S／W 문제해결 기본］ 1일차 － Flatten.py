for i in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    
    for _ in range(n):
        arr.sort()
        arr[-1] -= 1
        arr[0] += 1
    
    print(f'#{i}', max(arr) - min(arr))