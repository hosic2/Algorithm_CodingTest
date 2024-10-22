while True:
    temp = list(map(int, input().split()))
    if temp[0] == 0 and temp[1] == 0 and temp[2] == 0:
        break
    
    temp.sort()

    if temp[2] >= temp[1] + temp[0]:
        print('Invalid')
    elif temp[0] == temp[2]:
        print("Equilateral")
    elif temp[0] != temp[1] != temp[2]:
        print("Scalene")
    else:
        print("Isosceles")