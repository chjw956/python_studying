"""
# BFS(너비 우선 탐색) 예제

아래는 연결되어 있는 두 개 정점 사이의 간선을 순서대로 나열해 둔 것이다. 
모든 정점을 너비우선탐색(BFS)하여 경로를 출력하여라. (시작 정점은 1로 한다)

# 입력 값
1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7

# 출력 값
1 - 2 - 3 - 4 - 5 - 7 - 6

"""


# G: 그래프, v: 탐색 시작점, n: 정점의 개수
def bfs(G, v, n):
    visited = [0] * (n + 1)
    # 큐 생성
    queue = []

    # 시작점 v를 큐에 삽입
    queue.append(v)
    visited[v] = True

    # 큐가 비어있지 않는 동안
    while queue:
        # 큐의 첫 번째 원소를 반환 -> dequeue()
        t = queue.pop(0)
        # 방문하지 않은 곳인 경우,
        if not visited[t]:
            # 정점 t에서 할 일 수행
            # visit(t)

            # t와 연결된 모든 정점에 대해
            for i in G[t]:
                # 방문되지 않은 곳이라면
                if not visited[i]:
                    # 큐에 넣기
                    queue.append(i)
                    # 방문한 곳으로 표시해둠
                    visited[t] = True
            print(t, end = ' ')


def visit(t):
    pass


# 입력 데이터
input_data = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'

# 7개의 노드로 구성
N = 7

# 그래프 생성
graph = [[] for i in range(N + 1)]
arr = list(map(int, input_data.split()))

for i in range(0, len(arr) - 1, 2):
    v1, v2 = arr[i], arr[i + 1]
    graph[v1].append(v2)
    graph[v2].append(v1)

# bfs 탐색 실시
bfs(graph, 1, N)
