from heapq import heappush, heappop


def prim(start):
    heap = list()           
    MST = [0] * (V)                 # visited라고 생각하면 됨

    # 최소 비용 합계
    sum_weight = 0

    # 힙에서 관리해야 할 데이터
    # 가중치, 정점 정보
    # 정점 번호를 기준으로 정렬되기 때문에 이렇게 하면 안됨
    # heappush(heap, (start, 0))    
    heappush(heap, (0, start))      # 시작점은 가중치가 0임     

    while heap:
        weight, v = heappop(heap)
        
        # 이미 방문한 지점이면 통과
        if MST[v]:
            continue

        # 방문 처리
        MST[v] = 1
        # 누적합 추가
        sum_weight += weight

        # 갈수 있는 노드를 보면서
        for next in range(V):
            # 갈 수 없는 지점이면 continue
            if graph[v][next] == 0:
                continue

            # 이미 방문한 지점이면 continue
            if MST[next]:
                continue

            heappush(heap, (graph[v][next], next))

    return sum_weight

# V는 정점의 개수, E는 간선의 개수
V, E = map(int, input().split())
# 현재는 인접 행렬로 구현되어 있는데, 이것을 인접 리스트로 변경하는 것을 과제로 내주심
graph = [[0] * (V) for _ in range(V)] 
for _ in range(E):
    u, v, w = map(int, input().split())
    
    graph[u][v] = w
    graph[v][u] = w  # 가중치가 있는 무방향 그래프

result = prim(0)
print(f'최소 비용 = {result}')

'''
# 입력
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''
