X = int(input())
sticks = [64, 32, 16, 8, 4, 2 ,1]
count = 0

for i in sticks:
    if X >= i:
        X -= i
        count += 1
    
    if X == 0:
        break
        
print(count)      