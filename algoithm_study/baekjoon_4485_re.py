# 백준 4485. 녹색 옷 입은 애가 젤다지? (gold 4)
# NxN 크기의 동굴의 [0, 0]에서 주인공 링크가 동굴의 [N-1, N-1]까지 이동하려고 한다.
# 동굴은 각 칸마다 도둑루피가 있는데, 이 칸을 지나면 해당 도둑루피의 크기만큼 소지한 루피를 잃게 된다.
# 잃는 금액을 최소로 하여 동굴을 건너려고 할 때, 링크가 잃을 수밖에 없는 최소 금액은 얼마인가?
# (단, 링크는 상하좌우 인접한 곳으로 1칸씩 이동할 수 있다.)

import sys
sys.stdin = open('sample_input\sample_input(25).txt', 'r')
import heapq


def dijkstra(si, sj):
    pq = []

    heapq.heappush(pq, (cave[si][sj], (si, sj)))
    distance[si][sj] = cave[si][sj]
    
    # 우선순위 큐가 빌 때까지 반복함
    while pq:
        dist, (vi, vj) = heapq.heappop(pq)

        # 현재 노드가 이미 처리된 노드라면 skip
        if distance[vi][vj] < dist:
            continue

        # 현재 노드와 연결된 다른 인접 노드 확인
        for di, dj in directions:
            ni = vi + di
            nj = vj + dj

            if 0 <= ni < N and 0 <= nj < N:
                cost = cave[ni][nj]
                new_dist = dist + cost

                # 다음 노드를 가는 데 더 많은 비용이 드는 경우
                if new_dist >= distance[ni][nj]:
                    continue

                distance[ni][nj] = new_dist
                heapq.heappush(pq, (new_dist, (ni, nj)))
    


T = int(input())

# 아래쪽, 오른쪽 방향
directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

for tc in range(1, T + 1):
    N = int(input())
    cave = [list(map(int, input().split())) for _ in range(N)]

    # 누적 거리 저장 테이블
    distance = [[float('inf')] * N for _ in range(N)]
    roots = []

    # 1. 가능한 루트 리스트 모두 생성
    dijkstra(0, 0)

    min_cost = distance[N - 1][N - 1]
    
    print(f'Problem {tc}: {min_cost}')
