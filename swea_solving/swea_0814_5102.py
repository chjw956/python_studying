# SWEA 24.08.14.(수) 5102.[파이썬 S/W 문제해결 기본] 6일차 - 노드의 거리 (D2)
import sys
sys.stdin = open('sample_input\sample_input(29).txt', 'r')
    

# graph: 그래프, start: 탐색 시작점, n: 정점의 개수
def bfs(graph, n, start, goal):
    # 1. 방문 체크 리스트 생성
    visited = [0] * (n + 1)
    num = 1

    # 2. 큐 생성
    queue = []

    # 3. 시작점 v를 큐에 삽입함
    queue.append((start, [start]))
    visited[start] = num                      # 첫 번째로 방문한 레이어라는 의미

    # 4. 큐가 비어있지 않는 동안
    while queue:
        # 4-1. 큐의 첫 번째 원소를 반환함 -> dequeue()
        (t, path) = queue.pop(0)

        if t == goal:
            return path
            
        # 4-2-3. t와 연결된 모든 정점에 대해
        for i in graph[t]:
            # 4-2-3-1. 방문하지 않은 곳이라면 큐에 넣음
            if not visited[i]:
                num += 1
                queue.append((i, path + [i]))
                # 4-2-1. 방문한 곳으로 표시해둠
                visited[i] = num
    
    # 경로를 찾지 못했다면 0을 반환
    return 0


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)

    S, G = map(int, input().split())
    
    rslt = bfs(graph, V, S, G)

    if rslt == 0:
        print(f'#{tc} 0')        
    else:
        print(f'#{tc} {len(rslt) - 1}')