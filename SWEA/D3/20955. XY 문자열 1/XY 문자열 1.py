def dfs(current, target):
    if len(current) < len(target):
        return False
    if current == target:
        return True

    res = False
    if current[-1] == 'X':
        res |= dfs(current[:-1], target)
    if current[-1] == 'Y':
        res |= dfs(current[:-1][::-1], target)
    return res

T = int(input())
for i in range(1, T + 1):
    S = input().strip()
    E = input().strip()
    print(f'#{i}', "Yes" if dfs(E, S) else "No")  # E에서 S로 줄여나감
