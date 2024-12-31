n = int(input())
cnt, temp = 0, set()

for _ in range(n):
    i = input()
    if i == 'ENTER':
        temp.clear()
    elif i not in temp:
        cnt += 1
        temp.add(i)

print(cnt)