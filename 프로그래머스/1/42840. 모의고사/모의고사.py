def solution(answers):
    s1 = [1, 2, 3, 4, 5]
    s2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    count = [0,0,0]
    result = []
    
    for i in range(len(answers)):
        if answers[i] == s1[(i % len(s1))]:
            count[0] += 1
        if answers[i] == s2[(i % len(s2))]:
            count[1] += 1
        if answers[i] == s3[(i % len(s3))]:
            count[2] += 1
            
    for i in range(3):
        if count[i] == max(count):
            result.append(i + 1)

    return result