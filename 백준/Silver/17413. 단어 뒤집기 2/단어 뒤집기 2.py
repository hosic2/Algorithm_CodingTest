import sys
from collections import deque

input = sys.stdin.readline

char_queue = deque(input().strip())

while char_queue:
    string = ""
    if char_queue[0] == '<':
        while char_queue[0] != '>':
            string += char_queue.popleft()
        string += char_queue.popleft()
        print(string, end='')
    else:
        while len(char_queue) > 0 and char_queue[0] not in ['<', ' ']:
            string += char_queue.popleft()
        string = string[::-1]
        if len(char_queue) == 0 or char_queue[0] != ' ':
            print(string, end='')
        else:
            print(string, end=char_queue.popleft())