from itertools import permutations


def solution(k, dungeons):
    answer = 0
    for order in permutations(dungeons, len(dungeons)):
        tmp = k
        tired = 0
        
        for i in range(len(dungeons)):
            if order[i][0] <= tmp:
                tmp -= order[i][1]
                tired += 1
                
        answer = max(answer,tired)
        
    return answer