t = int(input())

def calc(n):
    if n == 10:
        return 1
    elif n == 20:
        return 3
    
    return calc(n - 10) + 2* calc(n - 20)

for i in range(t):
    n = int(input())
    
    print(f'#{i + 1}', calc(n))