for _ in range(10):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    answer = 0
    
    for i in range(100):
        answer = max(sum(arr[i]), sum(row[i] for row in arr), answer)
                     
    temp1 = 0
    for i in range(100):
        temp1 += arr[i][i]
                 
    temp2 = 0
    for i in range(100):
        temp2 += arr[i][99 - i]
                    
    print(f'#{n}', max(answer, temp1, temp2))