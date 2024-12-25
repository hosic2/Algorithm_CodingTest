n = int(input())

for _ in range(n):
    word = input()
    temp = []
    for i in word:
        if i == ')':
            if temp and temp[-1] == '(':
                temp.pop()
                continue
        temp.append(i)
    print('NO' if temp else 'YES')