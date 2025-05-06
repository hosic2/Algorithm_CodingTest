from collections import deque

t = int(input())

for n in range(t):
    stack = deque()
    word = input()
    flag = True

    for i in word:
        if i == '{' or i == '(':
            stack.append(i)
        elif i == '}':
            if not stack or stack[-1] != '{':
                flag = False
                break
            stack.pop()
        elif i == ')':
            if not stack or stack[-1] != '(':
                flag = False
                break
            stack.pop()

    if stack:
        flag = False

    print(f'#{n + 1}', 1 if flag else 0)