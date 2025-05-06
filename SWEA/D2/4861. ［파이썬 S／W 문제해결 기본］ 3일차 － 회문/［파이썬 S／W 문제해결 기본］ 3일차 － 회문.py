t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    answer = ''
    # 세로 회문 확인을 위해 한번에 다 받기
    word = [input() for _ in range(n)]
    
    for num in range(n):
    	# 가로 확인
        for j in range(n - m + 1):
            temp = word[num][j : j + m]
            if temp == temp[::-1]:
                answer = temp
                break
                
         # 세로 확인
        for j in range(n - m + 1):
            temp = ''.join(word[j + k][num] for k in range(m))
            if temp == temp[::-1]:
                answer = temp
                break
        
        if answer != '':
            break
    print(f'#{i + 1}', answer)