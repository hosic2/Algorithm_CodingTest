T = input()
l = sorted(map(int, input().split()))

answer = 0
total = 0

for i in l:
    total += i
    answer += total
    
print(answer)