def solution(price, money, count):
    answer = sum(i for i in range(price, price * count + 1, price))
    return answer - money if answer - money > 0 else 0