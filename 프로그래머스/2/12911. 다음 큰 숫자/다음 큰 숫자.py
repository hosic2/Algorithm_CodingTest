def solution(n):
    answer = n + 1
    n_count = bin(n).count('1')
    
    while True:
        if n_count == bin(answer).count('1'):
            return answer
        answer += 1