# BAEKJOON 1238. 파티 (gold 3)
# 시간 제한: 1초
# N개의 숫자로 구분된 각각의 마을에 한 명의 학생이 살고 있다고 할 때,
# N명의 학생이 마을에서 출발하여 M개의 단방향 도로들을 지나서 파티에 참석하고자 한다.
# 단방향 도로로 이루어져 있으므로 각 학생마다 경로가 달라짐에 유의하여 
# 왕복하는 데 가장 많은 시간을 소비한 학생의 이동 시간을 출력하라.
# (단, 도시 A에서 도시 B로 가는 도로의 개수는 최대 1개이다.)

import heapq


def dijkstra(s, sc, t):
    pq = []

    # heapq에 리스트로 저장할 때에는 맨 앞의 데이터를 기준하여 정렬됨
    heapq.heappush(pq, (sc, s))

    # 우선순위 큐가 빌 때까지 반복함
    while pq:
        # 가장 최단 거리인 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(pq)

        # 목적지 노드라면, 탐색 종료
        if now == t:
            break

        # 현재 노드가 이미 처리됐다면 skip
        if distance[now] < dist:
            continue

        # 현재 노드가 연결된 다른 인접 노드 확인
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            # 현재까지의 누적 가중치 + 다음 노드 가중치
            new_cost = dist + cost

            # 다음 노드로 가는 데 더 많은 비용이 드는 경우
            if new_cost >= distance[next_node]:
                continue
            
            # 다음 노드까지 가는 데 드는 비용 정보 저장
            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))


# N: 학생과 마을의 수, M: 단방향 도로 개수, X: 파티 장소 도시
N, M, X = map(int, input().split())

# 인접리스트 만들기(인접 노드 정보 저장)
graph = [[] for _ in range(N + 1)]

# (단방향 그래프) 간선 정보 입력
for _ in range(M):
    s, e, c = map(int, input().split())
    graph[s].append([e, c])

costs = [[0, float('inf')]] * (N + 1)

for n in range(1, N + 1):
    # 파티 장소로 go!
    # 목적지까지의 누적 거리를 저장할 테이블
    distance = [float('inf')] * (N + 1)    
    distance[n] = 0
    dijkstra(n, distance[n], X)
    dist1 = distance[X]

    # 집으로 다시 복귀!
    # 목적지까지의 누적 거리를 저장할 테이블
    distance = [float('inf')] * (N + 1)    
    distance[X] = dist1
    dijkstra(X, distance[X], n)
    costs[n] = [n, distance[n]]

costs.sort(key = lambda x:x[1])

print(costs[-2][1])