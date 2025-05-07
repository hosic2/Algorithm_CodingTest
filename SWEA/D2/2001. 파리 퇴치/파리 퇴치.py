t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
        
    answer = 0
    for x in range(n - m + 1):
        for y in range(n - m + 1):
            temp_sum = 0
            for dx in range(m):
                for dy in range(m):
                    temp_sum += arr[x + dx][y + dy]
            answer = max(answer, temp_sum)
            
    print(f'#{i + 1}', answer)