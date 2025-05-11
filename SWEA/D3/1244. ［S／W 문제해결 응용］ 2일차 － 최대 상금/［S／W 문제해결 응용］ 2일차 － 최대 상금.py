def dfs(n, lst, N, L, visited):
    global answer
    if n == N:  # 교환 횟수가 N에 도달하면 최종 결과 확인
        answer = max(answer, int("".join(lst)))
        return
    
    # 가능한 모든 교환을 시도
    for i in range(L - 1):
        for j in range(i + 1, L):
            lst[i], lst[j] = lst[j], lst[i]  # i, j 자리를 교환
            num = ''.join(lst)  # 숫자판을 문자열로 변환하여 비교
            
            # 이미 방문한 상태인지 체크 (교환 횟수와 숫자판 상태를 함께 체크)
            if (n + 1, num) not in visited:
                visited.add((n + 1, num))  # 방문한 상태로 기록
                dfs(n + 1, lst, N, L, visited)  # DFS 재귀 호출
            
            lst[i], lst[j] = lst[j], lst[i]  # 교환을 되돌림


T = int(input())

for test_case in range(1, T + 1):
    st, t = map(str, input().split())
    N = int(t)  # 최대 교환 횟수
    lst = list(st)  # 숫자판을 리스트로 변환
    L = len(lst)  # 숫자판 길이
    answer = 0  # 최종 결과를 담을 변수
    visited = set()  # 방문한 상태를 기록하는 set

    visited.add((0, ''.join(lst)))  # 초기 상태를 방문한 상태로 기록
    dfs(0, lst, N, L, visited)  # DFS 탐색 시작
    print(f"#{test_case} {answer}")