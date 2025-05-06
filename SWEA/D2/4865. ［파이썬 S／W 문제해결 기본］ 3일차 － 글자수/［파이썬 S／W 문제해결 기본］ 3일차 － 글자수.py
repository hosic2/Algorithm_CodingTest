from collections import Counter

t = int(input())

for i in range(t):
    n, m = input(), input()
    
    n_max = 0
    count = Counter(m)
    
    for j in n:
        temp = count[j]
       	if temp > n_max:
            n_max = temp
            
    print(f'#{i + 1}', n_max)