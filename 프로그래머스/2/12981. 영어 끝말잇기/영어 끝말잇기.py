def solution(n, words):
    temp = [words[0]]
    for i in range(1, len(words)):
        if words[i] in temp or temp[-1][-1] != words[i][0]:
            return [(i % n) + 1, (i // n) + 1]
        else:
            temp.append(words[i])
    return [0, 0]