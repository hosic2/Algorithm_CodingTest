t = int(input())

for x in range(1, t + 1):
    n = input()
    card = set()
    cnt = {'S': 13, 'D': 13, 'H': 13, 'C': 13}
    
    flag = True
    for i in range(0, len(n), 3):
        temp = n[i  : i + 3]
        if temp in card:
            flag = False
            break
        card.add(temp)
        cnt[temp[0]] -= 1
    
    print(f'#{x}', f"{cnt['S']} {cnt['D']} {cnt['H']} {cnt['C']}" if flag else "ERROR")