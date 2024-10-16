# 백준 11052. 카드 구매하기 (silver1)
# 카드 1개가 포함된 카드팩부터 카드 N개가 포함된 카드팩까지 총 N가지가 있다고 한다.
# 카드는 총 8가지의 종류가 있다.
# 민규는 카드의 개수가 적은 팩이더라도 가격이 비싸면 높은 등급의 카드가 많이 들어있을 것이라는 미신을 믿는다고 할 때,
# 민규가 돈을 최대한 많이 지불해서 카드를 N개 구매하려고 한다면 민규가 지불해야 하는 금액의 최댓값을 구하라.
# 단, N개보다 많은 개수의 카드를 산 후에 몇 장의 카드를 버려서 N장으로 맞추는 것은 불가능하다.
# 즉 구매한 카드팩에 포함된 카드 개수의 합이 N과 같아야만 한다.
# 시간 제한 1초

import sys
sys.stdin = open('sample_input\sample_input(22).txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    # N: 구매하고자 하는 카드 개수
    N = int(input())
    price = [0]
    # (index + 1)개의 카드로 구성된 카드팩마다의 가격
    price += [i for i in list(map(int, input().split()))]

    d = [0] * (N + 1)
    d[1] = price[1]

    for i in range(2, N + 1):
        values = []
        for j in range(1, i + 1):
            values += [d[i - j] + price[j]]
        d[i] = max(values)

    print(d[N])