t = int(input())

for x in range(1, t + 1):
    n = int(input())
    a = list(input().split())
    answer = []

    mid = (n + 1) // 2 # 홀수 시에 앞이 더 많은 것으로 설정
    
    for i in range(n // 2):
        answer.append(a[i])
        answer.append(a[i + mid])
    
    if n % 2 == 1:
        answer.append(a[mid - 1])
    
    print(f'#{x}', *answer)