# SWEA 24.08.07.(수) 12630. 4871. [파이썬 S/W 문제해결 기본] 4일차 - 그래프 경로

# 추천 문제: 오셀로 게임

# 인접 리스트를 사용하면 될 듯!

import sys
sys.stdin = open('.\sample_input\sample_input(20).txt', 'r')

T = int(input())


def DFS(graph, s, g, visited):
    visited[s] = True
    # print(s, end = ' ')
    if s == g:
        return

    for i in graph[s]:
        if not visited[i]:
            DFS(graph, i, g, visited)
    

for test_case in range(1, T + 1):
    # V개 이내의 노드를 E개의 간선으로 연결한 방향성 그래프 정보 입력
    V, E = map(int, input().split())

    graph = [[] * _ for _ in range(V + 1)]
    visited = [False] * (V + 1)

    # E개의 줄에 걸쳐, 출발 도착 노드의 간선 정보가 주어짐
    for _ in range(E):
        s, d = map(int, input().split())

        # 그래프 생성
        graph[s].append(d)

    # print(f'graph = {graph}')

    # E개의 줄 이후에 경로의 출발 노드(S), 도착 노드(G)가 주어짐
    S, G = map(int, input().split())
    
    print(f'#{test_case}', end = ' ')

    DFS(graph, S, G, visited)

    if visited[S] == True and visited[G] == True:
        print(1)
    else:
        print(0)