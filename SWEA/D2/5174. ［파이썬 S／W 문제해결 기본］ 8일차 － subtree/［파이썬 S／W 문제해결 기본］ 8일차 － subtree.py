t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))
    answer = [m]
    
    for j in range(0, len(nums), 2):
        if nums[j] in answer:
            answer.append(nums[j + 1])
            
    print(f'#{i + 1}', len(answer))