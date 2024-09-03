# 동전 교환 문제
# 1730원을 거슬러주기 위해 사용할 수 있는 최소 동전의 개수는?

# coin_list = [500, 100, 50, 10]
# target = 1730

# cnt = 0
# for coin in coin_list:
#     # 해당 동전에 대해 사용 가능한 수 
#     possible_cnt = target // coin

#     # 사용 가능한 수를 총 개수에 추가
#     cnt += possible_cnt
#     # 목표 금액에서 해당 금액만큼을 제외시킴
#     target -= coin * possible_cnt

# print(cnt)


# Fractional Knapsack 소스코드
n = 3
target = 30                                     # Knapsack kg 제한
things = [(5, 50), (10, 60), (20, 140)]         # (kg, price)

# (price / kg) 기준으로 내림차순
things.sort(key = lambda x:(x[1]/x[0]), reverse = True)

sum = 0
for kg, price in things:
    per_price = price / kg

    # 만약 가방에 남은 용량이 얼마되지 않는다면,
    # 물건을 잘라 가방에 넣고 끝냄
    if target < kg:
        sum += target * per_price
        break

    sum += price
    target -= kg

print(int(sum))             # 220