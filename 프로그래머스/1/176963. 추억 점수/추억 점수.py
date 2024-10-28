def solution(name, yearning, photo):
    answer = []
    zipper = dict(zip(name, yearning))
    
    for i in photo:
        temp = 0
        for j in i:
            if j in zipper:
                temp += zipper[j]
        answer.append(temp)
    return answer