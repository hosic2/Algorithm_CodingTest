T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    heights = list(map(int, input().split()))
    max_height = max(heights)

    grow_one = 0
    grow_two = 0

    for h in heights:
        diff = max_height - h
        grow_two += diff // 2
        grow_one += diff % 2

    min_pair = min(grow_one, grow_two)
    grow_one -= min_pair
    grow_two -= min_pair
    days = min_pair * 2

    if grow_one > 0:
        days += grow_one * 2 - 1
    else:
        total_two = grow_two * 2
        days += (total_two // 3) * 2 + (total_two % 3)

    print(f"#{tc} {days}")
