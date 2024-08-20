# SWEA 24.08.09.(금) - 12673. [파이썬 S/W 문제해결 기본] 5일차 토너먼트 카드게임 (D2)
# 만약 같은 카드인 경우 편의상 번호가 작은 쪽(순서가 빠른 쪽)을 승자라고 한다.
# 토너먼트 구현

import sys
sys.stdin = open('sample_input\sample_input(34).txt', 'r')


# 재귀로 구현
def winnerWho(lst, start, end, stack):
    n = end - start
    print(f'n = {n} = {end} - {start}, lst = {lst}')

    # 인원이 2명인 경우
    if n == 2:
        
        lst.sort(key=lambda x:x[1])
        big = lst[1][1]
        small = lst[0][1]

        rslt = big / small

        if rslt <= 2:
            stack.append(lst[1])
        else:
            stack.append(lst[0])
        return stack
    
    # 인원이 3명 이상인 경우
    elif n >= 3:
        winnerWho(lst[start : start + n // 2], start, start + n // 2, stack)
        winnerWho(lst[start + n // 2 : end], start + n // 2, end, stack)

    return stack


T = int(input())

for tc in range(1, 2):
    N = int(input())            # 인원 수 N
    # 1은 가위, 2는 바위, 3은 보
    cards = list(enumerate(list(map(int, input().split()))))   # 카드의 인덱스값과 데이터를 튜플로 변환하여 저장      

    n = N
    my_stack = []
    
    while len(cards) > 1:
        cards = winnerWho(cards, 0, n, my_stack)
        n = len(cards)
        
    
    print(f'#{tc} {cards}')