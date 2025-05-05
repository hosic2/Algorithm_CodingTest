t = int(input())

for i in range(t):
    num = float(input())
    answer = ''
    
    while len(answer) <= 12 and num != 0:
        num *= 2
      
        if num >= 1:
            answer += '1'
            num -= 1
        else:
            answer += '0'
            
    if len(answer) > 12:
        print(f'#{i+1} overflow')
    else:
        print(f'#{i+1} {answer}')