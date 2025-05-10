def min_insertions_to_make_palindrome(s: str) -> int:
    # 1. 이미 회문이면
    if s == s[::-1]:
        return 0

    # 2. x가 없고 회문도 아니면
    if 'x' not in s:
        return -1

    # 3. 투 포인터 접근
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
            return -1  # 중간에 x를 삽입해도 맞출 수 없음

    return cnt

T = int(input())
for _ in range(T):
    s = input().strip()
    print(min_insertions_to_make_palindrome(s))