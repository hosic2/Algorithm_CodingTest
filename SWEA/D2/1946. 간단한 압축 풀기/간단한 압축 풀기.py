t = int(input())

for x in range(1, t + 1):
    n = int(input())
    word = ''
    
    for _ in range(n):
        i, j = input().split()
        word += i * int(j)
    
    print(f'#{x}')
    for i in range(0, len(word), 10):
        print(word[i : i + 10])