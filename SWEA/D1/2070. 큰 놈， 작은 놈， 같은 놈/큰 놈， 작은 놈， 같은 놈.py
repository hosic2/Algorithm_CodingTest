t = int(input())

for i in range(1, t + 1):
    a, b = map(int, input().split())
    answer = ''
    
    if a > b:
    	answer = '>'
    elif a < b:
        answer = '<'
    else:
        answer = '='
        
    print(f'#{i}', answer)