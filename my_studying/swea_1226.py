# SWEA 1226. 미로1 (D4)
# 16x16 크기의 미로에서 0은 길, 1은 벽, 3은 도착점을 의미할 때,
# 미로의 시작점 (1, 1)에서 도착점까지 갈 수 있는 길이 있는지 판단하라.
# 도달 가능하다면 1을, 그렇지 않다면 0을 출력하라.

import sys
sys.stdin = open('sample_input\sample_input(1).txt', 'r')
from collections import deque


def bfs(si, sj, visited):
    global success
    # 시작점 방문 표시
    visited[si][sj] = 1

    q = deque([[si, sj]])

    while q:
        [vi, vj] = q.popleft()

        for [di, dj] in directions:
            ni = vi + di
            nj = vj + dj

            if 0 <= ni < 16 and 0 <= nj < 16 and matrix[ni][nj] != 1:
                if matrix[ni][nj] == 3:
                    success = 1
                    return
                if not visited[ni][nj]:
                    visited[ni][nj] = visited[vi][vj] + 1
                    q.append([ni, nj])


directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

for _ in range(10):
    tc = int(input())
    matrix = [list(map(int, input())) for _ in range(16)]
    # print(matrix)

    success = 0
    visited = [[0] * 16 for _ in range(16)]

    bfs(1, 1, visited)

    print(f'#{tc} {success}')