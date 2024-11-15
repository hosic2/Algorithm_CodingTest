def solution(sizes):
    # 큰 값 중 가장 큰 값 * 작은 값 중 가장 큰 값
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)