import sys

input = sys.stdin.readline
n = int(input())
stack = []
answer = []
flag = True
count = 1

for _ in range(n):
    num = int(input())

    while count <= num:
        stack.append(count)
        answer.append('+')
        count += 1

    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        flag = False
        break

if not flag:
    print("NO")
else:
    for i in answer:
        print(i)