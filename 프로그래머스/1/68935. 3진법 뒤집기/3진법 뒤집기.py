def solution(n):
    answer = 0
    temp = ''
    while n > 0:
        temp += str(n % 3)
        n = n // 3
    temp = temp[::-1]
    
    for i, v in enumerate(temp):
        answer += int(v) * (3 ** i)
    return answer