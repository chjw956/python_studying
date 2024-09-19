# BAEKJOON 1261. 알고스팟
# NxM 미로에서 알고스팟 운영진은 항상 같은 방에 있어야 한다.
# 이동 가능한 방향은 상하좌우이며, 빈방으로만 갈 수 있지만 AOJ 무기를 이용하여 벽을 부수고
# 빈방으로 만들어 그쪽으로 이동할 수도 있다.
# 현재 (1, 1)에 위치한 알고스팟 운영진이 (N, M)으로 이동하려면 벽을 최소 몇 개 부수어야 하는지 구하라.
# 시간 제한: 1초
# BFS 사용 풀이 (제한 시간 초과로 틀림)

from collections import deque
import sys
sys.stdin = open('sample_input\sample_input(17).txt', 'r')


def bfs(si, sj, visited):
    visited[si][sj] = 0

    queue = deque([[si, sj]])

    while queue:
        vi, vj = queue.popleft()
        
        for di, dj in direction:
            ni = vi + di
            nj = vj + dj

            if ni == M - 1 and nj == N - 1:
                visited[M - 1][N - 1] = min(visited[M - 1][N - 1], visited[vi][vj])
                continue
            
            # 미로 안에 위치하고
            if 0 <= ni < M and 0 <= nj < N:
                # 1. 방문하지 않은 곳인 경우
                if visited[ni][nj] == -1:
                    # 1-1. 벽이 위치한 칸인 경우
                    if miro[ni][nj] == 1:
                        visited[ni][nj] = visited[vi][vj] + 1
                    # 1-2. 빈 공간인 경우
                    else:
                        visited[ni][nj] = visited[vi][vj]
                    queue.append([ni, nj])
                # 2. 방문했던 곳인 경우
                else:
                    # 2-1. 벽이 위치한 칸인 경우
                    if miro[ni][nj] == 1:
                        visited[ni][nj] = min(visited[ni][nj], visited[vi][vj] + 1)
                    # 2-2. 빈 공간인 경우
                    else:
                        visited[ni][nj] = min(visited[ni][nj], visited[vi][vj])


T = int(input())

for tc in range(1, T + 1):
    # N: 열의 개수, M: 행의 개수
    N, M = map(int, input().split())
    miro = [list(map(int, input())) for _ in range(M)]

    # 상 하 좌 우
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    si = sj = 0

    visited = [[-1] * N for _ in range(M)]
    visited[M - 1][N - 1] = float('inf')

    bfs(si, sj, visited)

    print(visited[M- 1][N - 1])