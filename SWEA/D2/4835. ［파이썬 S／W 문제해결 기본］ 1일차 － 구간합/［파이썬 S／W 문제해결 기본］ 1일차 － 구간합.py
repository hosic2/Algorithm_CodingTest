t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    
    n_min = n_max = sum(nums[0:m])
    
    for j in range(1, n - m + 1):
        sector_sum = sum(nums[j : j + m])
        if sector_sum < n_min:
            n_min = sector_sum
        if sector_sum > n_max:
            n_max = sector_sum
            
    print(f'#{i+1}', n_max - n_min)