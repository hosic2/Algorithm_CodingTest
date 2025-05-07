t = int(input())

for i in range(t):
    arr = list(map(int, input().split()))
    
    # 파이썬 사사오입 방지 -> 그냥 round 테스트 했는데 통과해버림 ;
    print(f'#{i + 1}', int(sum(arr) / len(arr) + 0.5))