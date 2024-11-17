def solution(a, b, n):
    answer = 0
    
    while n >= a:
        ex_bottle = n // a
        new_coke = ex_bottle * b
        n = n - a * ex_bottle + new_coke
        answer += new_coke
    return answer