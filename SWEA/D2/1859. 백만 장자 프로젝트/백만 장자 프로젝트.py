t = int(input())

for i in range(t):
    n = input()
    nums = list(map(int, input().split()))
    answer = 0
    max_price = 0
    
    for j in nums[::-1]:
        if j > max_price:
            max_price = j
        else:
            answer += max_price - j
    
    print(f'#{i + 1}', answer)