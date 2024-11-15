def solution(sizes):
    w_max, h_max = 0, 0
    
    for i in sizes:
        w_max = max(w_max, max(i[0], i[1]))
        h_max = max(h_max, min(i[0], i[1]))
        
    return w_max * h_max