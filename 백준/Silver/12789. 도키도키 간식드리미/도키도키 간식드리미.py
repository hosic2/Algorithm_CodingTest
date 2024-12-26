n = input()
students = list(map(int, input().split()))
stack = []
seq = 1

for i in students:
    stack.append(i)
    
    while stack and stack[-1] == seq:
        stack.pop()
        seq += 1
        
print('Sad' if stack else 'Nice')