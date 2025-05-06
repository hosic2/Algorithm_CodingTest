t = int(input())

for i in range(t):
    e, n = map(int, input().split())
    nums = list(map(int, input().split()))
    tree = {}

    # 트리 구성: 부모를 키로, 자식 리스트를 값으로
    for j in range(0, len(nums), 2):
        p, c = nums[j], nums[j + 1]
        if p in tree:
            tree[p].append(c)
        else:
            tree[p] = [c]

    # DFS 정의
    def dfs(node):
        count = 1  # 자기 자신
        if node in tree:
            for child in tree[node]:
                count += dfs(child)
        return count

    print(f'#{i + 1}', dfs(n))