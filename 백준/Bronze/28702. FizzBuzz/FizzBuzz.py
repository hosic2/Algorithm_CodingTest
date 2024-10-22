answer = 0
for i in range(3, 0, -1):
    temp = input()

    if temp not in ['Fizz', 'Buzz', 'FizzBuzz']:
        answer = int(temp) + i

if answer % 15 == 0:
    print('FizzBuzz')
elif answer % 3 == 0:
    print('Fizz')
elif answer % 5 == 0:
    print('Buzz')
else:
    print(answer)