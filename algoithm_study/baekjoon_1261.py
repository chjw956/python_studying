# BAEKJOON 1261. 알고스팟
# NxM 미로에서 알고스팟 운영진은 항상 같은 방에 있어야 한다.
# 이동 가능한 방향은 상하좌우이며, 빈방으로만 갈 수 있지만 AOJ 무기를 이용하여 벽을 부수고
# 빈방으로 만들어 그쪽으로 이동할 수도 있다.
# 현재 (1, 1)에 위치한 알고스팟 운영진이 (N, M)으로 이동하려면 벽을 최소 몇 개 부수어야 하는지 구하라.

import heapq

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[si][sj] = 0

    while pq:
        dist, ni, nj = heapq.heappop(pq)
        if distance[ni][nj] < dist:
            continue

        for next in graph[ni][nj]:
            next_node = next[0]
            cost = next[1]

            new_cost = dist + cost
            
            if new_cost >= distance[next_node]:
                continue

            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))

N, M = map(int, input().split())
miro = [list(map(int, input().split())) for _ in range(N)]

# 상 하 좌 우
direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
si = sj = 0

distance = [[INF] * N for _ in range(M)]

dijkstra(start)

for i in range(N):
    for j in range(M):
        if distance[i][j] != INF:

             