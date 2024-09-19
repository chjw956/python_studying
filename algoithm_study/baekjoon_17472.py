# BAEKJOON 17472. 다리 만들기2 (gold 1)
# 참고 사이트: https://velog.io/@khc41/%EB%B0%B1%EC%A4%80-17472%EB%B2%88-%EB%8B%A4%EB%A6%AC-%EB%A7%8C%EB%93%A4%EA%B8%B0-2-C-%EC%82%BC%EC%84%B1-%EA%B8%B0%EC%B6%9C
# 제한시간 1초, 메모리 제한 512MB
# N x M의 지도에서 모든 섬을 다리로 연결하려고 한다.
# 다리의 양 끝은 섬과 인접한 바다 위에 있어야 하며, 다리의 모양은 직선 모양이다(가로/세로)
# 다리 길이는 최소 2 이상이어야 한다.
# 모든 섬을 연결하는 다리 길이의 최소값을 구하라. 불가능하다면 -1을 출력하라.

import sys
sys.stdin = open('sample_input\sample_input(19).txt', 'r')
from collections import deque


def bfs(si, sj, visited, empty):
    global island_cnt
    visited[si][sj] = island_cnt

    queue = deque([[si, sj]])
    empty.append([si, sj])

    while queue:
        [vi, vj] = queue.popleft()

        for di, dj in direction:
            ni = vi + di
            nj = vj + dj

            # 지도 범위 안에 있고 땅인 경우,
            if 0 <= ni <N and 0 <= nj < M and map_data[ni][nj]:
                if not visited[ni][nj]:
                    visited[ni][nj] = visited[vi][vj]
                    empty.append([ni, nj])
                    queue.append([ni, nj])
    return empty


# 간선 확인
def checkEdge():
    for k, v in island.items():
        min_row = min(v, key = lambda x:x[0])[0]        
        max_row = max(v, key = lambda x:x[0])[0]     

        min_col = min(v, key = lambda x:x[1])[1]     
        max_col = max(v, key = lambda x:x[1])[1]     

        min_dist = float('inf')
        approach = 0

        for i in range(min_row, max_row + 1):
            for j in range(0, min_col):
                if visited[i][j]:
                    dist = min_col - j - 1
                    if dist < min_dist:
                        min_dist = dist
                        approach = visited[i][j]        # 도달한 섬의 번호를 저장함

            if min_dist > 1 and min_dist != float('inf') and approach != 0:
                if [k, approach, min_dist] not in edge:
                    edge.append([k, approach, min_dist])

            min_dist = float('inf')
            approach = 0

            for j in range(max_col + 1, M):
                if visited[i][j]:
                    dist = j - max_col - 1
                    if dist < min_dist:
                        min_dist = dist
                        approach = visited[i][j]        # 도달한 섬의 번호를 저장함
                if min_dist > 1 and min_dist != float('inf') and approach != 0:
                    if [k, approach, min_dist] not in edge:
                        edge.append([k, approach, min_dist])

            min_dist = float('inf')
            approach = 0
        
        for j in range(min_col, max_col + 1):
            for i in range(0, min_row):
                if visited[i][j]:
                    dist = min_row - i - 1
                    if dist < min_dist:
                        min_dist = dist
                        approach = visited[i][j]

            if min_dist > 1 and min_dist != float('inf') and approach != 0:
                if [k, approach, min_dist] not in edge:
                    edge.append([k, approach, min_dist])

            min_dist = float('inf')
            approach = 0

            for i in range(max_row + 1, N):
                if visited[i][j]:
                    dist = i - max_row - 1
                    if dist < min_dist:
                        min_dist = dist
                        approach = visited[i][j]
            
            if min_dist > 1 and min_dist != float('inf') and approach != 0:
                if [k, approach, min_dist] not in edge:
                    edge.append([k, approach, min_dist])


def find_set(x):
    if parents[x - 1] == x:
        return x
    
    parents[x - 1] = find_set(parents[x - 1])       # 더이상 부모가 없을 때까지 가장 높은 부모를 찾음
    return parents[x - 1]


def union(x, y):
    x = find_set(x)
    y = find_set(y)            

    if x < y:
        parents[y - 1] = x
    else:
        parents[x - 1] = y

            
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]

T = int(input())

for tc in range(1, T + 1):
    # N: 세로 크기, M: 가로 크기
    N, M = map(int, input().split())

    map_data = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    island = dict()
    island_cnt = 1
    result = 0

    # 1. 섬 번호 매기기
    for i in range(N):
        for j in range(M):
            # 땅이고 방문한 적이 없는 곳이라면,
            if not visited[i][j] and map_data[i][j]:
                island[island_cnt] = bfs(i, j, visited, [])
                island_cnt += 1
    
    # 2. 간선 집합 생성
    edge = []
    checkEdge()
    edge.sort(key = lambda x:x[2])

    parents = [i for i in range(1, island_cnt)]
    cnt = 0

    for s, e, d in edge:
        if find_set(s) != find_set(e):
            cnt += 1
            union(s, e)
            result += d
            if cnt == island_cnt - 2:
                break

    parent = find_set(1)
    for n in range(2, island_cnt):
        if find_set(n) != parent:
            result = -1
            break
    
    print(result)