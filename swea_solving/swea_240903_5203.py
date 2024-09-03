# SWEA 24.09.03.(화) - 5203.[파이썬 S/W 문제해결 구현] 3일차 - 베이비진 게임 (D3)
# 0~9 카드 4set에서 6개의 카드를 골랐을 때, 연속인 숫자가 3개 이상이면 "run"이고
# 같은 숫자가 3개 이상이면 "triplet"이다.
# 플레이어 2명이 교대로 한 장씩 카드를 뽑을 때, 6장을 채우기 전이라도 run 또는 triplet이 되면 승자가 된다.
# 두 사람이 가져가는 순서대로 12장의 카드 정보가 주어질 때, 승자를 알아내는 프로그램을 작성하라.
# 무승부인 경우 0을 출력한다.

import sys
sys.stdin = open('sample_input\sample_input(50).txt', 'r')


def isItTriplet(cards):
    for i in range(len(cards)):
        same = 1
        for j in range(i + 1, len(cards)):
            if cards[i] == cards[j]:
                same += 1
                if same == 3:
                    return True
    return False


def isItRun(cards):
    for i in range(len(cards) - 2):
        for j in range(i + 1, len(cards) - 1):
            if abs(cards[j] - cards[i]) == 1 and cards[j + 1] - cards[j] == cards[j] - cards[i]:
                return True
    return False


T = int(input())

for tc in range(1, T + 1):
    card_list = list(map(int, input().split()))
    card_num = len(card_list)

    winner = 0

    a_cards = []
    b_cards = []

    print(f'#{tc}', end = ' ')

    for i in range(card_num):
        # 플레이어1 (a)
        if i % 2 == 0:
            a_cards.append(card_list[i])
            a_cards.sort()
            if isItRun(a_cards) or isItTriplet(a_cards):
                winner = 1
                break
        # 플레이어2 (b)
        else:
            b_cards.append(card_list[i])
            b_cards.sort()
            if isItRun(b_cards) or isItTriplet(b_cards):
                winner = 2
                break
    print(winner)