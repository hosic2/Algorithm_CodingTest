def solution(participant, completion):
    p_dict = {}
    for i in participant:
        p_dict[i] = p_dict.get(i, 0) + 1
        
    for i in completion:
        p_dict[i] -= 1
        
    return [i for i, v in p_dict.items() if v > 0][0]