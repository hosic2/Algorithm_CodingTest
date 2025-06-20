def gcd(n,m) :
    while m > 0 :
        n, m = m, n%m
    return n

def lcm(n,m) :
    return n*m / gcd(n,m)

def solution(n,m) :
    answer = []
    answer.append(gcd(n,m))
    answer.append(lcm(n,m))
    
    return answer