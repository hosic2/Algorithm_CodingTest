def solution(cacheSize, cities):
    answer = 0
    
    if cacheSize == 0:
        return len(cities) * 5
    
    cities = list(map(str.upper, cities))
    temp = []
    
    for i in cities:
        if i not in temp:
            if len(temp) == cacheSize:
                temp.pop(0)
            temp.append(i)
            answer += 5
        else:
            answer += 1
            temp.remove(i)
            temp.append(i)
            
    return answer