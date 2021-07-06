import sys

prices = [7,1,5,3,6,4]
#prices.sort()
# 1 3 4 5 6 7

profit = 0
min_price = sys.maxsize

for price in prices:
    min_price = min(min_price, price)
    profit = max(profit, price-min_price)
print(profit)