def solution(babbling):
    words = ["aya", "ye", "woo", "ma"]
    cnt = 0
    for b in babbling:
        for w in words:
            if not w * 2 in b:
                b = b.replace(w, ' ') 
        if b.isspace():
            cnt += 1
    return cnt