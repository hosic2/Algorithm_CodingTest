n = int(input())
n_list = list(map(int, input().split()))
answer = []

for i in range(len(n_list)):
    answer.insert(len(answer) - n_list[i], i + 1)

print(*answer)