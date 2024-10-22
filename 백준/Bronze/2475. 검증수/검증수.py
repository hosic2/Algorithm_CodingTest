numbers = list(map(int, input().split()))
answer = 0
answer += sum(i**2 for i in numbers)
print(answer % 10)