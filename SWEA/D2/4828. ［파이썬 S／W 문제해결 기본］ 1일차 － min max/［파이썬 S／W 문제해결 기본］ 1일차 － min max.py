t = int(input())

for i in range(t):
    # 필요 없는 수 -> 입력만 받기
    n = input()
    n_list = list(map(int, input().split()))
    
    print(f'#{i + 1}', max(n_list) - min(n_list))