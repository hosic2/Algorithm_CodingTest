import sys
input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort()

print(round(sum(lst)/n))
print(lst[n//2])

cnt = {}
for i in lst:
    cnt[i] = cnt.get(i, 0) + 1

mx = max(cnt.values())
mx_lst = [k for k, v in cnt.items() if v == mx]

print(mx_lst[0] if len(mx_lst) == 1 else mx_lst[1])
print(max(lst) - min(lst))