import math
from collections import deque

def solution(progresses, speeds):
    answer = []
    remain = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    
    queue = deque(remain)
    
    while queue:
        curr = queue.popleft()
        count = 1
        
        while queue and queue[0] <= curr:
            queue.popleft()
            count += 1
            
        answer.append(count)
        
    return answer