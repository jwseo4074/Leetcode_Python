prices = [7,1,5,3,6,4]
#prices.sort()
# 1 3 4 5 6 7

min_price = prices[0]
# 처음 값으로 설정

answer = 0
for i in range(len(prices)):
    min_price = min(min_price, prices[i])
    # 배열 돌면서 가장 낮은 가격 찾음
    profit = prices[i] - min_price
    # 그 인덱스에서 가장 낮은 가격과의 차이
    answer = max(answer, profit)
    # 최대 이익 갱신
print(answer)