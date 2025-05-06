t = int(input())

for i in range(t):
    n, m = input(), input()
    answer = 0
    
    if n in m:
        answer = 1
        
    print(f'#{i + 1}', answer)