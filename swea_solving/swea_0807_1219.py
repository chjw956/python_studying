# SWEA 24.08.07.(수) 1219.[S/W 문제해결 기본] 4일차 - 길찾기
# DFS에서 다시 부모 노드로 돌아오지 않는 조건만 추가해주면 되겠는디..?

import sys
sys.stdin = open('sample_input\sample_input(22).txt', 'r')

def modified_dfs(graph, s, g, visited)


for _ in range(1, 11):
    tc, num = map(int, input().split())
    graph = [[] for _ in range(100)]
    visited = [False] * 100

    coordinates = list(map(int, input().split()))

    for i in range(0, len(coordinates), 2):
        graph[coordinates[i]].append(coordinates[i + 1])

    


    print(f'#{tc} {result}')