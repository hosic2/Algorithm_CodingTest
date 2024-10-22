n = input()

numbers = []

for i in n:
    numbers.append(int(i))

numbers = sorted(numbers)[::-1]

print(''.join(str(i) for i in numbers))