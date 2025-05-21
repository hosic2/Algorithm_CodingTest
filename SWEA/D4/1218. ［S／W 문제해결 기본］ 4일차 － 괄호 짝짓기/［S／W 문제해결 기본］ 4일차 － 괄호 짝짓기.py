for x in range(1, 11):
    n = int(input())
    word = input()
    stack = []
    pair = {')': '(', ']': '[', '}': '{', '>': '<'}

    for ch in word:
        if ch in pair.values():  # 여는 괄호
            stack.append(ch)
        elif ch in pair:  # 닫는 괄호
            if stack and stack[-1] == pair[ch]:
                stack.pop()
            else:
                stack.append(ch)  # 짝 안 맞는 괄호 (오류 표시용)
                break

    print(f'#{x} {0 if stack else 1}')