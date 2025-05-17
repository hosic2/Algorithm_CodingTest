t = int(input())

for x in range(1, t + 1):
    n = input()
    print(f'#{x}', *sorted(list(map(int, input().split()))))