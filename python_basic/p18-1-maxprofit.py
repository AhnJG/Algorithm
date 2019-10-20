#주식 가격에서 최대 수익 구하기

def max_profit(stock):
    n = len(stock)
    max_profit = 0
    min_price = stock[0]

    for i in range(1, n):
        profit = stock[i] - min_price
        if profit > max_profit:
            max_profit = profit
        if stock[i] < min_price:
            min_price = stock[i]

    return max_profit

stock = [10300, 9600, 9800, 8200, 7800, 8300, 9500, 9800, 10200, 9500]
print(max_profit(stock))