# SWEA A형 대비 1 1953. [모의 SW 역량테스트] 탈주범 검거
# 숫자 1 ~ 7은 해당 위치의 터널 구조물 타입을 의미
# 숫자 0은 터널이 없는 장소임을 나타냄
# 탈주범이 탈출 한 시간 뒤 도달할 수 있는 지점은 한 곳임
# 탈주범이 위치할 수 있는 장소의 개수를 출력하는 프로그램을 작성하라.

import sys
sys.stdin = open('sample_input\sample_input(5).txt', 'r')
from collections import deque

# si: 시작점 행 정보, sj: 시작점 열 정보, time: 이동할 수 있는 시간(횟수)
def bfs(graph, si, sj, visited, time):
    global directions
    global classified

    # 현재 위치 방문 표시
    visited[si][sj] = 1

    queue = deque([[si, sj]])
    canGo = 1                               # 갈 수 있는 지점의 개수
    cnt = 1

    while queue and cnt < time:
        [vi, vj] = queue.popleft()

        # 해당 지점에서 갈 수 있는 방향 정보
        goList = classified[graph[vi][vj]]

        for g in goList:
            di = vi + directions[g][0]          # 갈 수 있는 지점의 i 좌표
            dj = vj + directions[g][1]          # 갈 수 있는 지점의 j 좌표

            # '하' 방향 진행이면 '상' 방향으로 받아야 하고,
            # '우' 방향 진행이면 '좌' 방향으로 받아야 함
            if g % 2 == 0:
                enter = g + 1
            else:
                enter = g - 1

            if 0 <= di < N and 0 <= dj < M:     # 지도 범위 내에 있고
                # 방문하지 않았으면서 파이프가 연결되어 있는 지점인 경우
                if not visited[di][dj] and enter in classified[graph[di][dj]]:  
                    if visited[vi][vj] + 1 == time:
                        return canGo
                    queue.append([di, dj]) 
                    visited[di][dj] = visited[vi][vj] + 1
                    canGo += 1   
                    cnt = visited[di][dj]
    
    return canGo

    
# 상(0) 하(1) 좌(2) 우(3) [i, j]
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

classified = { 0: [],
              1: [0, 1, 2, 3],          # 상하좌우
              2: [0, 1],                # 상하
              3: [2, 3],                # 좌우
              4: [0, 3],                # 상우
              5: [1, 3],                # 하우
              6: [1, 2],                # 하좌
              7: [0, 2]}                # 상좌

T = int(input())

for tc in range(1, T + 1):
    # N: 터널의 세로 크기
    # M: 터널의 가로 크기
    # R: 맨홀의 세로 위치
    # C: 맨홀의 가로 위치
    # L: 탈출에 소요되는 시간
    N, M, R, C, L = map(int, input().split())

    ternal = [list(map(int, input().split())) for _ in range(N)]
    visited = list([0] * M for _ in range(N))

    canGo = bfs(ternal, R, C, visited, L+1)

    print(f'#{tc} {canGo}')