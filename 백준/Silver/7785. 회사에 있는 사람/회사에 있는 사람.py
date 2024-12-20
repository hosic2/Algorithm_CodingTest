n = int(input())

s = set()

for _ in range(n):
    name, do = input().split()
    
    if do == 'enter':
        s.add(name)
    elif do == 'leave':
        s.remove(name)

for name in sorted(s, reverse=True):
    print(name)