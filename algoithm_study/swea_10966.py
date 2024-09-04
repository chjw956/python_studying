# SWEA 10966. 물놀이를 가자 (D4)
# 지도는 N x M 크기의 격자로 표현되고, W는 물 L은 땅을 의미한다.
# 어떤 칸에 사람이 있을 때, 상하좌우로 이동 가능하다고 하자.
# 이때 땅으로 표현된 모든 칸에 대해, 물인 칸으로 이동하기 위한 최소 이동 횟수의 합을 출력하라.

import sys
sys.stdin = open("sample_input\sample_input(6).txt", "r")

from collections import deque

def bfs(graph, visited):
    global directions
    global goal

    while goal:
        vi, vj = goal.popleft()
        
        for di, dj in directions:
            mi = vi + di
            mj = vj + dj
            # 지도상에 위치하고
            if 0 <= mi < N and 0 <= mj < M:
                # 땅(L)이면서 방문한 적이 없을 때,
                if graph[mi][mj] == 'L' and visited[mi][mj] == -1:
                # if graph[mi][mj] == 'L' and visited[mi][mj] > visited[vi][vj] + 1:
                    # 방문 표시
                    visited[mi][mj] = visited[vi][vj] + 1
                    goal.append([mi, mj])


# 상 하 좌 우
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

T = int(input())

for tc in range(1, T + 1):
    # N: 지도의 세로 크기, M: 지도의 가로 크기
    N, M = map(int, input().split())
    earth = [input() for _ in range(N)]
    visited = [[-1 for _ in range(M)] for __ in range(N)]

    # 지도에서 물(W)인 영역의 좌표 모음
    goal = deque([])
    for i in range(N):
        for j in range(M):
            if earth[i][j] == 'W':
                goal.append([i, j])
                visited[i][j] = 0

    # 물(W)인 영역에서 dfs를 사용해 각 지점까지의 최소 거리를 구함
    bfs(earth, visited)

    # visited에 표시된 최소 거리들을 더함
    sum_value = 0
    for i in range(N):
        sum_value += sum(visited[i])

    print(f'#{tc} {sum_value}')






"""
def bfs(graph, visited, n, m):
    queue = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'W':
                queue.append((i, j))
                visited[i][j] = 0

    while queue:
        x, y = queue.popleft()
        for d in directions:
            nx = x + d[0]
            ny = y + d[1]
            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                queue.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
 

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [input() for _ in range(n)]
    visited = [[-1] * m for _ in range(n)]
    
    # 상 하 좌 우
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    bfs(graph, visited, N, M)
    result = 0
    for i in range(N):
        result += sum(visited[i])
    print("#{} {}".format(tc, result))
"""
