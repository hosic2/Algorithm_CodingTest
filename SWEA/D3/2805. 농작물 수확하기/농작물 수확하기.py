t = int(input())

for i in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input().strip())) for _ in range(n)]
    answer = 0
    mid = n // 2
    
    for j in range(n):
        if j <= mid:
            answer += sum(arr[j][mid - j : mid + j + 1])
        else:
            answer += sum(arr[j][j - mid : n - (j - mid)])
        
    print(f'#{i}', answer)