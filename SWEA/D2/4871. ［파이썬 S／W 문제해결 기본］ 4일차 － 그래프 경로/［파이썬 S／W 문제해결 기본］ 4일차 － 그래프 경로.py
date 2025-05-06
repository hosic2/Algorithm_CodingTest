def dfs(graph, current, goal):
    if current == goal:
        return True
    for neighbor in graph.get(current, []):
        if neighbor not in visited:
            visited.add(neighbor)
            if dfs(graph, neighbor, goal):
                return True
    return False

T = int(input())
for t in range(1, T + 1):
    V, E = map(int, input().split())
    graph = {}

    for _ in range(E):
        u, v = map(int, input().split())
        graph.setdefault(u, []).append(v)

    S, G = map(int, input().split())
    visited = set([S])

    found = dfs(graph, S, G)
    print(f"#{t} {1 if found else 0}")
