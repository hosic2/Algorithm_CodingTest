num = int(input())

num_list = list(map(int, input().split()))

print(num_list[0] ** 2 if len(num_list) == 1 else min(num_list) * max(num_list))