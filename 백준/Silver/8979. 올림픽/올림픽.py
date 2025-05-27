N, K = map(int, input().split())
medals = [list(map(int, input().split())) for _ in range(N)]

medals.sort(key=lambda x: (x[1], x[2], x[3]), reverse=True)

rank = 1
same = 1

for i in range(N):
    if i > 0 and medals[i][1:] == medals[i-1][1:]:
        pass
    else:
        rank = i + 1
    if medals[i][0] == K:
        print(rank)
        break
