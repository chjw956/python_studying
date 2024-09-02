# SWEA 1244. [S/W 문제해결 응용] 2일차 - 최대 상금 (D3)
# 주어진 숫자판들 중 2개를 선택하여 정해진 횟수만큼 서로의 위치를 교환할 수 있다. (동일한 위치의 교환이 중복되어도 된다.)
# 교환이 끝난 후 각 위치에 부여된 가중치에 의해 상금이 계산된다. (왼쪽으로 갈수록 각 자리는 10의 배수만큼 가중치를 커진다.)
# 이때 상금으로 받을 수 있는 가장 큰 금액을 계산해보자.

# 순열 + 완전탐색 / 횟수는 어떻게 하지?

import sys
sys.stdin = open('sample_input\sample_input(8).txt', 'r')

# 정훈이 코드 참고
# 1. 교환 횟수만큼 교환했을 때의 최댓값을 비교함
def solution(cnt, num_list):
    global max_num

    # 교환 횟수를 채웠을 때, 
    if cnt == int(N):
        # 더 큰 수를 선택
        max_num = max(max_num, int(''.join(num_list)))
        return
    
    for i in range(len(num) - 1):
        for j in range(i + 1, len(num)):
            # 교환 수행
            num_list[i], num_list[j] = num_list[j], num_list[i]
            # 현재 수
            current_num = ''.join(num_list)

            # 2. 교환했을 때, 이미 비교된 값이라면 비교하지 말기
            if (cnt, current_num) not in visited:
                visited.add((cnt, current_num))
                print(f'visited = {visited}')
                solution(cnt + 1, num_list)

            num_list[i], num_list[j] = num_list[i], num_list[j]
        

T = int(input())

for tc in range(1, T + 1):
    max_num = 0

    # N: 교환 횟수
    num, N = input().split()
    num_list = list(num)

    # (횟수, 숫자)
    visited = set()

    solution(0, num_list)

    print(f'{tc} {max_num}')