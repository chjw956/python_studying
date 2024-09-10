# SWEA 1949. [모의 S/W 역량테스트] 등산로 조성 (D2)
# Python 15초, Java 3초
# N x N의 부지에 최대한 긴 등산로를 만들고자 한다.
# 등산로는 가장 높은 봉우리에서 시작하여 가장 낮은 지형으로 가로 또는 세로 방향으로 이어진다.
# 따라서 높이가 같은 곳 혹은 대각선 방향의 연결은 불가능하다.
# 긴 등산로를 만들기 위해 딱 한 곳에 대해 최대 K 깊이 만큼 지형을 깎을 수 있다.(1보다 낮게도 만들 수 있음)
# 이때 만들 수 있는 가장 긴 등산로를 찾아 그 길이를 출력하라.

import sys
sys.stdin = open('sample_input\sample_input(11).txt', 'r')

from collections import deque
from copy import deepcopy

# 가장 높은 봉우리 찾기
def findPeaks(arr, n):
    global high, highest, low, lowest
    for i in range(n):
        for j in range(n):
            if arr[i][j] > highest:
                highest = arr[i][j]
                high.append([i, j])
            if arr[i][j] < lowest:
                lowest = arr[i][j]
                low.append([i, j])


def dfs(arr, si, sj, visited, n, chance):
    global path
    visited[si][sj] = n
    path = max(path, n)

    for d in directions:
        ni = si + d[0]
        nj = sj + d[1]

        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            if arr[si][sj] > arr[ni][nj]:
                dfs(arr, ni, nj, visited, n + 1, chance)
            elif chance >= arr[ni][nj] - arr[si][sj] + 1:
                chance = 0
                dfs(arr, ni, nj, visited, n + 1, chance)


def bfs(arr, si, sj, visited, n, chance):
    global path, N
    visited[si][sj] = n
    
    queue = deque([[si, sj]])

    while queue:
        [vi, vj] = queue.popleft()
        for d in directions:
            ni = vi + d[0]
            nj = vj + d[1]

            if 0 <= ni < N and 0 <= nj < N:
                if arr[vi][vj] > arr[ni][nj]:
                    visited[ni][nj] = visited[vi][vj] + 1
                    queue.append([ni, nj])
                elif chance >= arr[ni][nj] - arr[vi][vj] + 1:
                    chance = 0
                    arr[ni][nj] = arr[vi][vj] - 1
                    visited[ni][nj] = visited[vi][vj] + 1
                    queue.append([ni, nj])
                path = max(path, visited[ni][nj])

                
# 상 하 좌 우
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

T = int(input())

for tc in range(1, T + 1):
    # N: 부지 크기, K: 깎을 수 있는 지형 높이
    N, K = map(int, input().split())
    ground = [list(map(int, input().split())) for _ in range(N)]

    # 1. 마지막으로 가장 높은 봉우리의 크기와 인덱스 값을 저장함
    # (가장 낮은 봉우리의 크기와 인덱스도 저장)
    high = []
    low = []
    highest = path = 0
    lowest = 9
    findPeaks(ground, N)

    # 2. 가장 높거나 낮은 봉우리의 값과 동일한 곳이 있는지를 확인
    for i in range(N):
        for j in range(N):
            if ground[i][j] == highest:
                high.append([i, j])
            if ground[i][j] == lowest:
                low.append([i, j])

    # 3. 찾은 시작점(높은 봉우리)들을 DFS + 백트래킹 알고리즘을 이용해 등산로 찾기
    for h in high:
        arr = deepcopy(ground)
        visited = [[0] * N for _ in range(N)]
        dfs(arr, h[0], h[1], visited, 1, K)
        # bfs(arr, h[0], h[1], visited, 1, K)
        
    print(f'#{tc} {path}')