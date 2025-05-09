import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = [0] + list(map(int, input().split()))
sum_arr = [0] * (n + 1)

for i in range(1, n + 1):
    sum_arr[i] = sum_arr[i - 1] + arr[i]
    
# max 값 설정하기 애매함 -> 리스트 하나 두고 max로 뽑기
temp = [] 
for i in range(k, n + 1):
    temp.append(sum_arr[i] - sum_arr[i - k])
    
print(max(temp))