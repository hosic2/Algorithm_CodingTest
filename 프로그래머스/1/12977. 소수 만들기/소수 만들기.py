from itertools import combinations

def solution(nums):
    answer = 0
    for c in combinations(nums, 3):
        s = sum(c)
        if all(s % i for i in range(2, int(s ** 0.5) + 1)):
            answer += 1
    return answer