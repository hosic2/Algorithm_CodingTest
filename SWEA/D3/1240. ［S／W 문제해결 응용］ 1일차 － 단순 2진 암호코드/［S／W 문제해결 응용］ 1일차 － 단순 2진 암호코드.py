num = {'0001101' : 0, '0011001' : 1, '0010011' : 2, '0111101' : 3, '0100011' : 4,
        '0110001' : 5,'0101111' : 6, '0111011' : 7, '0110111' : 8, '0001011' : 9}

t = int(input())

for i in range(1, t + 1):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    temp = []
    code = ''
    
    for j in range(n):
        if '1' in arr[j]:
            code = arr[j].rstrip('0')[-56:]
            break
     
    for j in range(len(code), len(code) - 56, -7):
        temp.insert(0, num[code[j - 7 : j]])
        
    calc = sum(temp[::2]) * 3 + sum(temp[1::2])
    
    print(f'#{i}', sum(temp) if calc % 10 == 0 else 0)