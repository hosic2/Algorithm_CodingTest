a_list = [1, 1, 2, 2, 2, 8]
b_list = list(map(int, input().split()))

for i in range(len(a_list)):
    print(a_list[i] - b_list[i], end=' ')