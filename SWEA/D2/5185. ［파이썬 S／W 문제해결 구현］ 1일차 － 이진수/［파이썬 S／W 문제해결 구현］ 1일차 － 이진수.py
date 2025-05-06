t = int(input())

for i in range(t):
    n, m = input().split()
    bin_num = bin(int(m, 16))[2:]
    
    print(f'#{i + 1}', '0' * ((4 - len(bin_num) % 4) % 4) + bin_num)