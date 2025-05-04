T = int(input())

for _ in range(T):
    temp = list(input().split())
    answer = []
    
    for i in temp:
        answer.append(i[::-1])
    
    print(" ".join(answer))