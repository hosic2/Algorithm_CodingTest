temp = []
n = int(input())

for _ in range(n):
    m = int(input())

    if m != 0:
        temp.append(m)
    elif len(temp) != 0 and m == 0:
        temp.pop()

print(sum(temp)) 