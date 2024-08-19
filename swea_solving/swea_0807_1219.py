# SWEA 24.08.07.(수) 1219.[S/W 문제해결 기본] 4일차 - 길찾기
# DFS에서 다시 부모 노드로 돌아오지 않는 조건만 추가해주면 되겠는디..?
from collections import deque
import sys
sys.stdin = open('sample_input\sample_input(22).txt', 'r')


# DFS 메서드
# 재귀로 DFS를 구현하면 실제 프로그램 수행 시간이 느려질 수 있다.
def dfs(graph, start, visited):
    # 현재 노드를 방문 처리
    visited[start] = 1
    print(start, end = ' ')

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문함
    for i in graph[start]:
        if not visited[start]:
            dfs(graph, i, visited)


# BFS 메서드
def bfs(graph, start, visited):
    # 큐(Queue) 구현을 위해  deque 라이브러리 사용
    queue = deque([start])

    # 현재 노드를 방문 처리
    visited[start] = 1

    # 큐가 빌 때까지 탐색을 반복함
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력함
        v = queue.popleft()
        print(v, end = ' ')
        
        
        # 방문 표시로 사용할 값을 1로 초기화함
        value = 2
        visited[v] = value

        if graph[v] == None:
            continue

        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입함
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = value
            value += 1

for _ in range(1, 11):
    tc, N = map(int, input().split())       # N : 길의 개수
    A = 0                       # 출발점(A)
    B = 99                      # 도착점(B)
    graph = [None] * 100
    visited = [0] * 100

    # 그래프 작성 (단방향)
    inputs = [int(i) for i in input().split()]
    for i in range(0, 2 * N, 2):
        if graph[i] == None:
            graph[inputs[i]] = [inputs[i + 1]]
        else: 
            graph[inputs[i]].append(inputs[i + 1])

    print(f'#{tc}', end = ' ')
    # BFS 호출
    bfs(graph, A, visited)
    print()


"""
# 답안
def dfs():
    start, end = 0, 99
    stack = [start]
    visited = [0] * 100
    visited[start] = 1
    
    while stack:
        current = stack[-1]
        if current == end : # 현재 위치가 찾는 목적지라면
            return 1    # 1반환
        for i in range(2):
            v = graph[i][current]   # 방문하려는 정점번호
            if v != -1 and not visited[v]:    #정점에 방문하지 않았으면 방문.
                stack.append(v)
                visited[v] = 1
                break
        else:   
            stack.pop()
    return 0


for _ in range(10):
    tc, E = map(int, input().split())
    # 그래프 저장하기
    graph = [[-1] * 100 for _ in range(2)]
    data = list(map(int, input().split()))
    for i in range(0, E * 2, 2):
        if graph[0][data[i]] == -1:
            graph[0][data[i]] = data[i + 1]
        else:
            graph[1][data[i]] = data[i + 1]

    result = dfs()
    print(f'#{tc} {result}')

"""
