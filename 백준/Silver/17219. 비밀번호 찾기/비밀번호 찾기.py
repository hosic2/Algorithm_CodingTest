N, M = map(int, input().split())

web = dict()

for _ in range(N):
    site, pw = input().split()
    
    web[site] = pw
    
for _ in range(M):
    print(web[input()])