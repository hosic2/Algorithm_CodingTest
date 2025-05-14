t = int(input())

for x in range(1, t + 1):
    n = int(input())
    seen = set()
    current = n

    while len(seen) < 10:
        seen.update(str(current))
        current += n

    print(f'#{x}', current - n)