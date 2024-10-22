n = int(input())
word = input()
sum = 0
for i in range(n):
    sum += (ord(word[i]) - 96) * 31**i

print(sum % 1234567891)