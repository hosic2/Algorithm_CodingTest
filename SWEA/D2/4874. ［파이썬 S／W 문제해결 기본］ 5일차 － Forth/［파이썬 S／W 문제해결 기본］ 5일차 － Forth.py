t = int(input())

for i in range(t):
    word = input().split()
    stack = []

    for token in word:
        if token == '.':
            if len(stack) == 1:
                print(f'#{i + 1}', stack.pop())
            else:
                print(f'#{i + 1} error')
            break
        elif token.isdigit():
            stack.append(token)
        else:
            if len(stack) < 2:
                print(f'#{i + 1} error')
                break
                
            b = int(stack.pop())
            a = int(stack.pop())
            
            if token == '+':
                stack.append(str(a + b))
            elif token == '-':
                stack.append(str(a - b))
            elif token == '*':
                stack.append(str(a * b))
            elif token == '/':
                stack.append(str(a // b))