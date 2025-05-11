T = int(input())

for t in range(1, T + 1):
    N, M, L = map(int, input().split())
    sequence = list(map(int, input().split()))
    
    for _ in range(M):
        index, value = map(int, input().split())
        sequence.insert(index, value)
        
    print(f'#{t}', sequence[L])