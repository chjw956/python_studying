# SWEA 24.08.14.(수) 5105. [파이썬 S/W 문제해결 기본] 6일차 - 미로의 거리 (D3)
# 미로에서 시작점의 데이터가 2이고 도착점의 데이터가 3일 때, 경로를 찾아라.

import sys
sys.stdin = open('sample_input\sample_input(30).txt', 'r')


# i: 시작점의 행 정보, j: 시작점의 열 정보, N: 행과 열의 크기
def bfs(i, j, N):
    global maze

    # 1. visited 생성
    visited = [[-1] * N for _ in range(N)]
    # 2. queue 생성
    queue = []
    # 3. 시작점 enQueue()
    queue.append([i, j])
    # 4. 시작점 방문 표시
    visited[i][j] = 0

    # 5. 탐색
    while queue:
        # dequeue()
        ti, tj = queue.pop(0)

        # 목적지에 도달했다면,
        if maze[ti][tj] == 3:
            # 도착지도 포함된 값이므로 1 빼줌
            return visited[ti][tj] - 1 
        
        # 델타 활용
        for di, dj in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            wi, wj = ti + di, tj + dj
            # 미로 내부에 존재하고, 인접한 벽이 아니고, 방문한 적이 없다면
            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != 1 and visited[wi][wj] == -1:
                # enQueue()
                queue.append([wi, wj])
                # 방문 표시
                visited[wi][wj] = visited[ti][tj] + 1
    
    # 경로를 찾지 못했다면 -1을 반환함
    return 0

# 입력된 미로에서 시작점을 찾는 함수
def find_start(N):
    global maze
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    
    st_i, st_j = find_start(N)
    ans = bfs(st_i, st_j, N) 

    print(f'#{tc} {ans}')