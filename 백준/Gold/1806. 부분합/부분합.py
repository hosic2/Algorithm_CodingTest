import sys

input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = 0
part_sum = 0
temp = []

while end <= n:
    if part_sum >= s:
        temp.append(end - start)
        part_sum -= arr[start]
        start += 1
    else:
        if end < n:
            part_sum += arr[end]
        end += 1

print(min(temp) if temp else 0)