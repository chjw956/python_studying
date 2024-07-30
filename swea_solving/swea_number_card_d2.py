# Solving club (00_SSAFY_12기_구미_2반)
# 24.07.30. 실습 및 과제(3)
# 1일차 - 숫자 카드(D2)

import sys
sys.stdin = open('sample_input(2).txt', 'r')

T = int(input())

for test_case in range(T):
    N = int(input())
    num = int(input())
    a_list = []

    while num >= 1:
        a_list.append(num % 10)
        num //= 10

    cards = [0] * 10

    for idx in range(len(a_list)):
        cards[a_list[idx]] += 1
    
    max_value = cards[0]
    max_index = 0

    # 개수가 같은 경우 숫자가 큰 것을 출력함
    for idx in range(len(cards)):
        if cards[idx] == max_value:
            max_index = idx
        if cards[idx] > max_value:
            max_value = cards[idx]
            max_index = idx

    print(f'#{test_case + 1} {max_index} {max_value}')
    