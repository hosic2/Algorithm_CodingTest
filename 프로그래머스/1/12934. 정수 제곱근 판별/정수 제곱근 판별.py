import math 

def solution(n):
    answer = pow(math.sqrt(n) + 1, 2) if math.sqrt(n).is_integer() else -1
    return answer