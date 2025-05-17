for x in range(1, 11):
    n = input()
    word = list(input().split())
    m = int(input())
    cmd = [(int(data[i+1]), int(data[i+2]), list(map(int, data[i+3:i+3+int(data[i+2])]))) for data in [input().split()] for i in range(len(data)) if data[i] == 'I']
    
    for pos, _, nums in cmd:
        word[pos:pos] = nums 

    print(f'#{x}', *word[:10])