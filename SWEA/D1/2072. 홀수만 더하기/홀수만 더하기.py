t = int(input())

for i in range(t):
    nums = list(map(int, input().split()))
    
    print(f'#{i + 1}', sum(j for j in nums if j %2 == 1))