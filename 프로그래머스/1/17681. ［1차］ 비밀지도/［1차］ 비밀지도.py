def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        answer.append(str(bin(arr1[i] | arr2[i]))[2:].rjust(n, '0').replace('1', '#').replace('0', ' ')) # rjust : n의 값을 길이로 갖도록 문자열 왼쪽을 '0'으로 채움
    return answer