def solution(elements):
    answer = []
    elements2 = elements * 2
    
    for i in range(len(elements)):
        for j in range(len(elements)):
            answer.append(sum(elements2[j : j + i + 1]))
            
    return len(set(answer))