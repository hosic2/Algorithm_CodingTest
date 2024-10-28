def solution(n, m, section):
    answer = 0
    current_pos = 0
    
    for i in section:
        if i > current_pos:
            answer += 1
            current_pos = i + m - 1
    
    return answer
