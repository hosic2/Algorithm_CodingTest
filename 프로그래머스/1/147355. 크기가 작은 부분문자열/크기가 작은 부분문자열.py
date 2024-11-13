def solution(t, p):
    answer = 0
    
    for i in range(len(p) - 1, len(t)):
        if p >= t[i - len(p) + 1 : i + 1] :
            answer += 1
    return answer