for t in range(1, 11):
    n = input()
    print(f'#{t}', sum(int(num) for num in input().split('+')))