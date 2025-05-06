def binary_search(p, target):
    l = 1
    r = p
    count = 0

    while l <= r:
        c = (l + r) // 2
        count += 1
        if c == target:
            return count
        elif c > target:
            r = c
        else:
            l = c

T = int(input())
for i in range(T):
    P, Pa, Pb = map(int, input().split())

    a_count = binary_search(P, Pa)
    b_count = binary_search(P, Pb)

    if a_count < b_count:
        winner = 'A'
    elif a_count > b_count:
        winner = 'B'
    else:
        winner = '0'

    print(f'#{i + 1}', winner)