grades = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
t = int(input())

for x in range(1, t + 1):
    n, k = map(int, input().split())
    l = []
    temp = 0
    
    for i in range(n):
        a, b, c = map(int, input().split())
        l.append(a * 0.35 + b * 0.45 + c * 0.2)
        if i == k - 1:
            temp = a * 0.35 + b * 0.45 + c * 0.2
    
    l.sort(reverse=True)
    rank = l.index(temp)
    grade_index = rank * 10 // n
    
    print(f'#{x}', grades[grade_index])