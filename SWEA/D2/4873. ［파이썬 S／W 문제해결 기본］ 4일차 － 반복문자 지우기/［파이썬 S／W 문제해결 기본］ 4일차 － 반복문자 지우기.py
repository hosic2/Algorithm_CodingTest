t = int(input())

for i in range(t):
    word = list(input())
    stack = []
    
    for j in word:
        if not stack:
            stack.append(j)
        else:
            if j == stack[-1]:
                stack.pop()
            else:
                stack.append(j)
    
    print(f'#{i + 1}', len(stack))