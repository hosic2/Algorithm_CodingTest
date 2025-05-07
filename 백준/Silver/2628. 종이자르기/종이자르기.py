w, h = map(int, input().split())
n = int(input())

w_list = [0, w]
h_list = [0, h]

for _ in range(n):
    i, j = map(int, input().split())
    
    if i == 0:
        h_list.append(j)
    elif i == 1:
        w_list.append(j)
        
w_list.sort()
h_list.sort()

answer = 0
for i in range(1, len(w_list)):
    for j in range(1, len(h_list)):
        w = w_list[i] - w_list[i - 1]
        h = h_list[j] - h_list[j - 1]
        answer = max(answer, w * h)

print(answer)