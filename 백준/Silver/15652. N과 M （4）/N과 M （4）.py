def dfs(k):
    if len(s) == m:
        print(' '.join(map(str, s)))
        return

    for i in range(k, n + 1):
        s.append(i)
        dfs(i)
        s.pop()


n, m = map(int, input().split())
s = []

dfs(1)