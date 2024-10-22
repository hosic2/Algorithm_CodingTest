n = int(input())

numbers = list(map(int, input().split())) 

sorted_unique_numbers = sorted(set(numbers))

rank = {value: index for index, value in enumerate(sorted_unique_numbers)}

result = [rank[i] for i in numbers]

for i in result:
    print(i, end=' ')
