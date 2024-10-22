import sys

def my_round(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return int(n)

n = int(sys.stdin.readline().strip())
if n:
    temp = []
    cut = my_round(n * 0.15)
    for _ in range(n):
        temp.append(int(sys.stdin.readline().strip()))
    temp.sort()
    if cut > 0:
        print(my_round(sum(temp[cut:-cut]) / len(temp[cut:-cut])))
    else:
        print(my_round(sum(temp) / len(temp)))
else:
    print(0)