t = int(input())

for i in range(1, t + 1):
    word = input()
    
    print(f'#{i}', 1 if word == word[::-1] else 0)