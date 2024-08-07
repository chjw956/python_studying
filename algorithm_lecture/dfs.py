# 24.08.06.(화) [DFS] 다음은 연결되어 있는 두 정점 사이의 간선을 순서대로 나열해둔 것이다. 
# 모든 정점을 깊이 우선 탐색(DFS)하여 화면에 경로를 출력하시오. (시작 정점은 1로 한다.)

"""
출력 결과
1 2 4 6 5 7 3
"""

"""
# 내가 끄적이던 코드

def dfs(graph):
    global top
    global my_stk
    global visited
    
    top += 1
    my_stk.append(graph.keys()[0])
    visited.append(graph.keys()[0])

    # 로직을 어떻게 짜야 하지?
    while True:
        top += 1
        my_stk.append(i for i in graph[my_stk[top-1]])

        

information = list(map(int, input().split()))           # 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7 입력
my_graph = dict()

# 입력된 값을 이용해 무방향 그래프 생성
for i in range(0, len(information), 2):
    if information[information[i]] in my_graph:
        my_graph[information[i]].append(information[i+1])
    else:
        my_graph[information[i]] = [information[i + 1]]

    if information[i + 1] in my_graph:
        my_graph[information[i + 1]].append(information[i])
    else:
        my_graph[information[i + 1]] = [information[i]]

my_stk = []             # 스택
top = -1
visited = []               # 방문한 정점

"""

"""
# 교수님 코드
# 스택 활용 방법
def DFS(s, V):                          # s: 시작정점, V: 정점 개수(1번부터인 정점의 마지막 정점)
    visited = [0] * (V + 1)             # 방문한 정점 표시
    stack = []                          # 스택 생성
    print(s, end =" ")
    visited[s] = 1                      # 시작정점 방문 표시

    v = s

    while True:
        for w in adjL[v]:               # v에 인접하고, 방문하지 않은 w가 있으면
            if visited[w] == 0:              
                stack.append(v)         # push(v) 현재 정점을 push하고
                v = w                   # w에 방문
                print(v, end = " ")
                visited[w] = 1          # w에 방문 표시
                break                   # v부터 다시 탐색함
        else:                           # 남은 인접정점이 없어서 break가 걸리지 않은 경우
            if stack: # 이전 갈림길을 스택에서 꺼내서 (if TOP > -1)
                v = stack.pop()
            else:                       # 되돌아갈 곳이 없으면 남은 갈림길이 없는 경우에 탐색을 종료함.
                break                   # while True:


T = int(input())

for test_case in range(1, T + 1):
    # E = V + 1인 건가?
    V, E = map(int, input().split())    # 7 8 입력
    adjL = [[] for _ in range(V + 1)]

    arr = list(map(int, input().split()))

    # 그래프 생성
    for i in range(E):
        v1, v2 = arr[i * 2], arr[i * 2 + 1]
        adjL[v1].append(v2)
        adjL[v2].append(v1)
    
    print(f'adjL = {adjL}')

    DFS(1, V)
"""

"""
# 재귀를 활용한 강사님 코드
def dfs2(v, visited):
    print(v, end = '')
    visited[v] = 1
    for i in range(1, V + 1):
        if adj[v][i] and not visited[i]:
            dfs2(i, visited)
"""

# 알고리즘 책 코드
def dfs(graph, v, visited):
    # 현재 노드를 방문 처리함
    visited[v] = True
    print(v, end=" ")

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문함
    for i in graph[v]:
        if not visited[v]:
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