def solution(absolutes, signs):
    answer = sum(i if j else -i for i, j in zip(absolutes, signs))
    return answer