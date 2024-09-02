# SWEA 7465. 창용 마을 무리의 개수 (D4)
# 두 사람이 서로 아는 관계이거나 몇 사람을 거쳐 알 수 있는 관계를 다 묶어서 하나의 무리라고 한다.
# 창용 마을에 몇 개의 무리가 존재하는지 계산하라.

import sys
sys.stdin = open('sample_input\sample_input(7).txt', 'r')

from collections import deque

def bfs(graph, start, visited):
    global group

    queue = deque([start])
    
    while queue:
        v = queue.popleft()
        visited[v] = group
        for n in graph[v]:
            if not visited[n]:
                visited[n] = visited[v]
                queue.append(n)
                

T = int(input())

for tc in range(1, T + 1):
    # N: 창용 마을에 사는 사람의 수, M: 서로를 알고 있는 사람의 관계 수
    N, M = map(int, input().split())
    group = 0

    network = [[] for _ in range(N + 1)]
    visited = [0 for _ in range(N + 1)]
    visited[0] = -1

    for _ in range(M):
        a, b = map(int, input().split())
        network[a].append(b)
        network[b].append(a)

    while visited.count(0) > 0:
        start = visited.index(0)
        group += 1 
        bfs(network, start, visited)
    
    print(f'#{tc} {group}')
        