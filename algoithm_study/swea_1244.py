# SWEA 1244. [S/W 문제해결 응용] 2일차 - 최대 상금 (D3)
# 주어진 숫자판들 중 2개를 선택하여 정해진 횟수만큼 서로의 위치를 교환할 수 있다. (동일한 위치의 교환이 중복되어도 된다.)
# 교환이 끝난 후 각 위치에 부여된 가중치에 의해 상금이 계산된다. (왼쪽으로 갈수록 각 자리는 10의 배수만큼 가중치를 커진다.)
# 이때 상금으로 받을 수 있는 가장 큰 금액을 계산해보자.

import sys
sys.stdin = open('sample_input\sample_input(8).txt', 'r')

# 정훈이 코드와 강사님 코드를 참고하였음

# N번 카드를 교환할 때까지 재귀적으로 수행
# idx: 카드를 교환한 횟수
def solve(idx):
    global max_result

    # 교환 횟수가 남아있지 않으면 종료
    if idx == N:        
        max_result = max(max_result, int(''.join(cards)))
        return

    # 모든 카드들에 대해 자신보다 뒤에 있는 카드들과 위치 변경
    for i in range(cards_num - 1):
        for j in range(i + 1, cards_num):
            cards[i], cards[j] = cards[j], cards[i]
            
            # 현재의 값 계산
            curr_num = ''.join(cards)
            
            # 교환했을 때, 과거에 비교되지 않은 값인 경우에만 계속 교환 진행
            if (idx, curr_num) not in visited:
                visited.add((idx, curr_num))
                solve(idx + 1)

            # 교환해봤으니 원래 모양대로 돌려놓기
            cards[i], cards[j] = cards[j], cards[i]


T = int(input())

for tc in range(1, T + 1):
    cards, N = input().split()
    cards = list(cards)             # 카드 리스트
    cards_num = len(cards)          # 카드 개수
    N = int(N)                      # 제한된 교환 횟수
    max_result = 0                  # 최대 상금

    # (횟수, 숫자) 저장
    visited = set()

    print(f'#{tc}', end = ' ')
    solve(0)
    print(max_result)