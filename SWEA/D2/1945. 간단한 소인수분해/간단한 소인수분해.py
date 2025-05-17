T = int(input())

primes = [2, 3, 5, 7, 11]

for tc in range(1, T + 1):
    N = int(input())
    result = []

    for p in primes:
        count = 0
        while N % p == 0:
            N //= p
            count += 1
        result.append(count)

    print(f'#{tc}', *result)