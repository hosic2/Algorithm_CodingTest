from collections import Counter

t = int(input())

for i in range(t):
    n = input()
    cards = list(map(int, input().strip()))  # 공백 없이 나열된 한자리 수 분리

    count = Counter(cards)
    max_freq = max(count.values())
    max_card = max([k for k, v in count.items() if v == max_freq])
        
    print(f'#{i + 1}', max_card, max_freq)