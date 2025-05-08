t = int(input())

for k in range(1, t + 1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    answer = 0
    
    # 두 리스트의 길이가 다를 경우, 작은 리스트의 길이에 맞게 계산
    if n > m:
        a, b = b, a 
        n, m = m, n 

    for i in range(m - n + 1):
        temp = 0
        for j in range(n):
            temp += a[j] * b[i + j]
        answer = max(answer, temp)
    
    print(f'#{k}', answer)