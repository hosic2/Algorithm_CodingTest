t = int(input())

for x in range(1, t + 1):
    n = input()
    cnt = 0
    prev = '0'

    for bit in n:
        if bit != prev:
            cnt += 1
            prev = bit

    print(f'#{x}', cnt)