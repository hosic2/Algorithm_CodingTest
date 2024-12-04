from collections import Counter


def solution(want, number, discount):
    answer = 0
    t_dict = {}
    
    for i in range(len(want)):
        t_dict[want[i]] = number[i]

    for i in range(len(discount) - 9):
        if t_dict == Counter(discount[i:i+10]): 
            answer += 1

    return answer