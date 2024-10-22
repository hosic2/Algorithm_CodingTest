n = int(input())
wordlist = []

for i in range(n):
    word = input()
    wordlist.append(word[:1] + word[-1:])

for i in wordlist:
    print(i)