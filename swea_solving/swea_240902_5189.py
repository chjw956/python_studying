# SWEA 5189.[파이썬 S/W 문제해결 구현] 2일차 - 전자카트 (D3)
# 사무실에서 출발해 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때 
# 전기 카트의 최소 배터리 사용량을 구하시오.
# 1번은 사무실, 2번 ~ N번은 관리 구역 번호이다.
# 완전탐색 실습

import sys
sys.stdin = open('sample_input\sample_input(49).txt', 'r')


def moveCart(start, using):
    global min_using
    
    # 관리 구역을 모두 방문했으면 종료
    if len(path) == N:
        min_using = min(min_using, using + ground[path[-1]][0])
        return
    
    for k in range(1, N):
        # 방문한 곳 제외        
        if k not in path:
            using += ground[start][k]
            path.append(k)
            moveCart(k, using)
        
            # 원래 모양대로 돌려놓기
            path.pop()
            using -= ground[start][k]


T = int(input())

for tc in range(1, T + 1):
    N = int(input())            # N: 관리 구역 수
    ground = [list(map(int, input().split())) for _ in range(N)]
    
    path = [0]                  # 경로
    min_using = 100 ** 2        # 최소 사용량

    moveCart(0, 0)

    print(f'#{tc} {min_using}')