def solution(left, right):
    return sum(-i if (i ** 0.5).is_integer() else i for i in range(left, right + 1)) #루트를 씌웠을 때 정수면 홀수 개
