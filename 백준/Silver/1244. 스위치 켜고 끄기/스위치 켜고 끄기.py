import sys

def switching(start, end, jump):
    for i in range(start, end, jump):
        switch[i] = 1 - switch[i]

input = sys.stdin.readline

n = int(input())
switch = list(map(int, input().split()))

for _ in range(int(input())):
    gender, num = map(int, input().split())
    num -= 1  # 인덱스 조정 (1번 스위치 → 0번 인덱스)

    if gender == 1:
        switching(num, n, num + 1)
    else:
        i = 1
        while num - i >= 0 and num + i < n and switch[num - i] == switch[num + i]:
            i += 1
        switching(num - i + 1, num + i, 1)

for i in range(n):
    print(switch[i], end=" ")
    if (i + 1) % 20 == 0:
        print()