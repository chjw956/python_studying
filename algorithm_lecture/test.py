# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]

# print(list(zip(di, dj)))

"""
# 비트맵 만들기
N = 5                                   # n : 원소의 개수

# 부분 집합의 개수만큼 반복
for i in range(1 << N):                 # 1 << n : 부분 집합의 개수
    for j in range(N-1, -1, -1):        # 원소의 수만큼 비트를 비교함
    # for j in range(N):        # 원소의 수만큼 비트를 비교함
        if i & (1 << j):                # i의 j번째 비트가 1이라면
            print(1, end = ", ")        
            # print(arr[j], end=", ")     # j번 원소 출력
        else:
            print(0, end = ", ")
    print()

"""

# a = b = 1
# a += 1
# b += 2
# print(a)
# print(b)


# from collections import defaultdict

# lst = [['a', 'b', 'c'], ['d', 'e', 'f']]

# dd = defaultdict(list)

# for i, j, k in lst:
#     dd[i].append((j, k))
#     dd[j].append((i, k))

# print(dd)


from heapq import heappush, heappop

def prim(start):
    heap = list()           
    MST = [0] * (V)                 # visited라고 생각하면 됨

    # 최소 비용 합계
    sum_weight = 0

    # 힙에서 관리해야 할 데이터
    # 가중치, 정점 정보
    # heappush(heap, (start, 0))    # 정점 번호를 기준으로 정렬되기 때문에 안됩니다.
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
