def solution(s, n):
    answer = ''
    
    for i in s:
        if i == ' ':
            answer += i
        elif i.islower() and chr(ord(i) + n) > 'z' or i.isupper() and chr(ord(i) + n) > 'Z':
            answer += chr(ord(i) - 26 + n)
        else:
            answer += chr(ord(i) + n)
            
    return answer