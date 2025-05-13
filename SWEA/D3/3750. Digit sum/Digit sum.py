t = int(input())
results = []

for x in range(1, t + 1):
    n = input().strip()
    
    while len(n) > 1:
        n = str(sum(int(ch) for ch in n))
    
    results.append(f'#{x} {n}')

print('\n'.join(results))