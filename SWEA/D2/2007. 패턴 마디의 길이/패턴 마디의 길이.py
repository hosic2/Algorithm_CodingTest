t = int(input())

for i in range(1, t + 1):
    word = input()
    
    for j in range(15):
        if word[0 : j + 1] == word[j + 1: (j + 1 ) * 2]:
            print(f'#{i}', len(word[0 : j + 1]))
            break