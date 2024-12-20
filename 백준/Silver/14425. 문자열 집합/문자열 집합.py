N, M = map(int, input().split())
s = set()
ans = 0

for _ in range(N):
    s.add(input().strip())
    
for _ in range(M):
    t = input().strip() 
    if t in s:
        ans += 1
print(ans)