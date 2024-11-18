def solution(k, tangerine):
    answer = 0
    
    t_dict = {}
    for i in tangerine:
        if i in t_dict :
            t_dict[i] += 1
        else:
            t_dict[i] = 1
    
    sorted_t = sorted(t_dict.items(), key=lambda x: x[1], reverse=True)
    
    while k > 0:
        count = sorted_t.pop(0)[1]
        k -= count
        answer += 1
    
    return answer