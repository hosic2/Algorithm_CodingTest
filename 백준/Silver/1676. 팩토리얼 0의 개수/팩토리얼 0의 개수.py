def factorial(n):
    if n > 1:
        return n * factorial(n - 1)
    else:
        return 1
    
fact = str(factorial(int(input())))[::-1]

count = 0
for i in fact:
    if i == '0':
        count += 1
    else:
        break
print(count)