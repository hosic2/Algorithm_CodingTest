import sys
from collections import Counter


def part_arr(arr):
    sub = []
    for i in range(len(arr)):
        total = 0
        for j in range(i, len(arr)):
            total += arr[j]
            sub.append(total)
    return sub


input = sys.stdin.readline

T = int(input())
n = int(input())
A = list(map(int, input().split()))
m = int(input())
B = list(map(int, input().split()))

# A, B의 부배열 합 전부 저장
A_sub = part_arr(A)
B_sub = part_arr(B)

# A의 부배열 합 빈도수 기록
A_count = Counter(A_sub)

# B의 부배열 합 순회하면서 (T - b)의 A 빈도수 더하기 -> A + B = T
result = 0
for b in B_sub:
    result += A_count[T - b]

print(result)