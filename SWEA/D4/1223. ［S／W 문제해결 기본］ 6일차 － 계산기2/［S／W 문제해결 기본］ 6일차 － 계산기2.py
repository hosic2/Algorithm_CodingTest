def calculate_expression(expression):
    stack = []  # 연산을 위한 스택
    operators = {'+', '*'}  # 지원되는 연산자
    precedence = {'+': 1, '*': 2}  # 연산자 우선순위

    num_stack = []  # 숫자 처리용 스택
    op_stack = []  # 연산자 처리용 스택
    
    # 숫자와 연산자 구분하여 처리
    for char in expression:
        if char.isdigit():  # 숫자일 경우
            num_stack.append(int(char))
        elif char in operators:  # 연산자일 경우
            while (op_stack and precedence[op_stack[-1]] >= precedence[char]):
                op = op_stack.pop()
                b = num_stack.pop()
                a = num_stack.pop()
                if op == '+':
                    num_stack.append(a + b)
                elif op == '*':
                    num_stack.append(a * b)
            op_stack.append(char)

    # 남은 연산자 처리
    while op_stack:
        op = op_stack.pop()
        b = num_stack.pop()
        a = num_stack.pop()
        if op == '+':
            num_stack.append(a + b)
        elif op == '*':
            num_stack.append(a * b)

    return num_stack[0]

# 입력 처리
T = 10  # 총 10개의 테스트 케이스
for t in range(1, T + 1):
    n = int(input())  # 테스트 케이스의 길이
    expression = input().strip()  # 중위 표기식 입력
    
    # 중위 표기식을 바로 계산
    result = calculate_expression(expression)
    
    # 결과 출력
    print(f"#{t} {result}")