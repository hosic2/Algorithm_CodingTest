from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    people = list(map(int, input().split()))
    
    counter = Counter(people)
    most_common = max(counter.values())
    max_score = max([k for k, v in counter.items() if v == most_common])
    
    print(f'#{n}', max_score)