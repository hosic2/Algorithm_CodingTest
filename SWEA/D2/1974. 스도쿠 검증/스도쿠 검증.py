t = int(input())
nums = [i for i in range(1, 10)]

for i in range(1, t + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    flag = 1
    
    for j in range(9):
        if sorted(arr[j]) != nums:
            flag = 0
            break
     
    for j in range(9):
        col = [arr[i][j] for i in range(9)]
        if sorted(col) != nums:
            flag = 0
            break
            
    for x in range(0, 9, 3):
        for y in range(0, 9, 3):
            temp = []
            for dx in range(x, x + 3):
                for dy in range(y, y + 3):
                    temp.append(arr[dx][dy])
            if sorted(temp) != nums:
                flag = 0
                break
           
    print(f'#{i}', flag)