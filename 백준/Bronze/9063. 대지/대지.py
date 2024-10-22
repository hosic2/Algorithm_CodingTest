n = int(input())

x, y = [], []

for _ in range(n):
    x_pot, y_pot = map(int, input().split())
    x.append(x_pot)
    y.append(y_pot)

print(((max(x) - min(x))) * ((max(y) - min(y))))