n = int(input())

temp = []

for _ in range(n):
    word = input()
    if word in temp:
        continue
    temp.append(word)

temp.sort(key=lambda x : (len(x), x))

for i in range(len(temp)):
    print(temp[i])