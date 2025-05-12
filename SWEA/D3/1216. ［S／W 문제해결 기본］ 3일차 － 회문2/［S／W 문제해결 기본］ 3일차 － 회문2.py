def check_palindrome(M, arr):
    for i in range(100):
        for j in range(100 - M + 1):
            if arr[i][j] == arr[i][j + M - 1]:
                if arr[i][j:j + M] == arr[i][j:j + M][::-1]:
                    return True

        for j in range(100 - M + 1):
            if arr[j][i] == arr[j + M - 1][i]:
                column = [arr[k][i] for k in range(j, j + M)]
                if column == column[::-1]:
                    return True

    return False

for x in range(1, 11):
    N = int(input()) 
    arr = [list(input()) for _ in range(100)]

    for M in range(100, 0, -1):
        if check_palindrome(M, arr): 
            print(f'#{N}', M)
            break