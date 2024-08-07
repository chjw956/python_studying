"""
# 인접 행렬
INF = 99999999      # 무한의 비용 선언

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
    [0, 7, 5],
    [7, 0, INF], 
    [5, INF, 0]
]

print(graph)


# 인접 리스트 예제

# 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0, 7))

# 노드 2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0, 5))

print(graph)

"""

# 알고리즘 책 코드
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리함
    visited[v] = True
    print(v, end=" ")

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문함
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# 각 노드가 연결된 정보를 2차원 리스트로 표현
graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

# 각 노드가 방문된 정보를 1차원 리스트로 표현
visited = [False] * 9

dfs(graph, 1, visited)