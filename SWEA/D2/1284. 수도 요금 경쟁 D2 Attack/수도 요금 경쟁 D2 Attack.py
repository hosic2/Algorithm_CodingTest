t = int(input())
for m in range(1, t + 1):
    p, q, r, s, w = map(int, input().split())
    print(f'#{m}', min(p * w, q if w <= r else q + (w - r) * s))