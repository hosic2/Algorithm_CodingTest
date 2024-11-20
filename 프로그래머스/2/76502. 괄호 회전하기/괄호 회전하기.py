def solution(s):
    answer = 0
    s = list(s)
    
    for _ in range(len(s)):
        stack = []
        for i in s:
            if len(stack) > 0:
                if stack[-1] == '[' and i == ']': 
                    stack.pop()
                elif stack[-1] == '{' and i == '}': 
                    stack.pop()
                elif stack[-1] == '(' and i == ')': 
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
        if len(stack) == 0:
            answer += 1
        s.append(s.pop(0))
        
    return answer