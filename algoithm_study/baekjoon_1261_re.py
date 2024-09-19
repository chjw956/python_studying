# dijkstra 이용 풀이
import heapq
import sys
sys.stdin = open('sample_input\sample_input(17).txt', 'r')


def dijkstra(si, sj):
    pq = []
    # heapq 에 리스트로 저장할 때는 맨 앞의 데이터를 기준으로 정렬된다.
    heapq.heappush(pq, (0, [si, sj]))
    distance[si][sj] = 0  # 시작 노드 최단 거리는 0

    # 우선순위 큐가 빌 때 까지 반복
    while pq:
        # 가장 최단 거리인 노드에 대한 정보 꺼내기
        dist, [vi, vj] = heapq.heappop(pq)
        # 현재 노드가 이미 처리됐다면 skip
        if distance[vi][vj] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드 확인
        for di, dj in direction:
            ni = vi + di
            nj = vj + dj 

            if 0 <= ni < M and 0 <= nj < N:
                cost = miro[ni][nj]

                new_cost = dist + cost  # 누적값(현재까지의 누적값 + 다음 노드 가중치)

                # 다음 노드를 가는 데 더 많은 비용이 드는 경우
                if new_cost >= distance[ni][nj]:
                    continue

                distance[ni][nj] = new_cost  # next_node 까지 가는데 비용은 new_cost
                heapq.heappush(pq, (new_cost, [ni, nj]))


T = int(input())

for tc in range(1, T + 1):
    # N: 열의 개수, M: 행의 개수
    N, M = map(int, input().split())
    miro = [list(map(int, input())) for _ in range(M)]

    # 상 하 좌 우
    direction = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    si = sj = 0
    distance = [[float('inf')] * N for _ in range(M)]

    dijkstra(si, sj)

    print(distance[M- 1][N - 1])