T, M = map(int, input().split())

l = []

for _ in range(T):
    t = int(input())
    if t <= M:
        l.append(t)
        
l.sort(reverse=True)
    
answer = 0
    
for i in l:
    if i <= M:
        answer += M // i
        M %= i
        
        if M == 0:
            break
            
print(answer)