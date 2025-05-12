def dfs(idx, score, calorie):
    global answer
    if calorie > l:
        return
    if idx == n:
        answer = max(answer, score)
        return
    
    # 재료 선택
    dfs(idx + 1, score + scores[idx], calorie + calories[idx])
    # 선택 X
    dfs(idx + 1, score, calorie)


t = int(input())

for k in range(1, t + 1):
    n, l = map(int, input().split())
    scores = []
    calories = []
    
    for _ in range(n):
        i, j = map(int, input().split())
        scores.append(i)
        calories.append(j)
    answer = 0
    dfs(0, 0, 0)
    print(f'#{k}', answer)