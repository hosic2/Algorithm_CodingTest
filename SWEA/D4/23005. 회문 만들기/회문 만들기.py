def calc(s):
    if s == s[::-1]:
        return 0
    if 'x' not in s:
        return -1

    left, right = 0, len(s) - 1
    cnt = 0

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        elif s[left] == 'x':
            left += 1
            cnt += 1
        elif s[right] == 'x':
            right -= 1
            cnt += 1
        else:
            return -1

    return cnt

T = int(input())
for _ in range(T):
    s = input().strip()
    print(calc(s))