import sys


input = sys.stdin.readline
s = input().strip()
q = int(input())
n = len(s)

# 알파벳 개수만큼 반복
count = [[0] * (n + 1) for _ in range(26)]

for i in range(n):
    char_idx = ord(s[i]) - ord('a')
    for j in range(26):
        count[j][i + 1] = count[j][i]
    count[char_idx][i + 1] += 1

# 문자 개수 확인
for _ in range(q):
    a, l, r = input().split()
    l, r = int(l), int(r)

    a_index = ord(a) - ord('a')

    print(count[a_index][r + 1] - count[a_index][l])