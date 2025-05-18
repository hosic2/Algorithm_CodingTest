for x in range(1, 11):
    _, m = input().split()
    stack = []
    
    for i in m:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)

    print(f'#{x}', ''.join(stack))