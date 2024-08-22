# 백준 10026번. 적록색약 (gold5)

# N X N 그리드의 그림에 대해 몇 개의 구역이 나누어지는데, 하나의 구역은 같은 색으로 이루어진다.
# 또한 같은 색상이 상하좌우로 인접해 있는 경우, 두 글자는 같은 구역에 속한다.
# 입력된 그림에 대해 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하라.
# R(빨강), G(초록), B(파랑)

from collections import deque


# def bfs(graph, searchPoints, visited, num):
#     start = searchPoints.pop()

#     if visited[start[0]][start[1]]:
#         return visited, searchPoints, num
    
#     num += 1
#     # 큐(Queue) 구현을 위해 deque 라이브러리 사용
#     queue = deque([start])
#     # 현재 노드 방문 처리
#     visited[start[0]][start[1]] = num

#     # 상 하 좌 우 [i + di, j + dj]
#     directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
#     # 큐가 빌 때까지 탐색함
#     while queue:
#         v = queue.popleft()
#         # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입함
#         for d in directions:
#             di = v[0] + d[0]
#             dj = v[1] + d[1]
#             if 0 <= di < N and 0 <= dj < N and not visited[di][dj]:
#                 if graph[v[0]][v[1]] == graph[di][dj]:
#                     queue.append([di, dj])
#                     visited[di][dj] = num
#                 elif (graph[v[0]][v[1]] == 'R' and graph[di][dj] == 'G') \
#                     or (graph[v[0]][v[1]] == 'G' and graph[di][dj] == 'R'):
#                         print(f'v = [{v[0]}][{v[1]}]')
#                         searchPoints.append([di, dj])
#                 else:
#                     searchPoints.append([di, dj])

#     return visited, searchPoints, num


# N = int(input())

# painting = []
# for _ in range(N):
#     painting.append(list(input()))

# visited = [[0] * N for _ in range(N)]
# searchPoints = [[0, 0]]
# num = 0

# while len(searchPoints) > 0:
#     visited, searchPoints, num= bfs(painting, searchPoints, visited, num)

# print(num)



# 실패작
# def bfs(graph, start, visited):
#     num = 1
#     # 큐(Queue) 구현을 위해 deque 라이브러리 사용
#     queue = deque([start])
#     # 현재 노드 방문 처리
#     visited[start[0]][start[1]] = num

#     # 상 하 좌 우 [i + di, j + dj]
#     directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
#     # 큐가 빌 때까지 탐색함
#     while queue:
#         print()
#         print(f'visited = {visited}')
#         print(f'queue = {queue}')
#         v = queue.popleft()
#         # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입함
#         for d in directions:
#             di = v[0] + d[0]
#             dj = v[1] + d[1]
#             if 0 <= di < N and 0 <= dj < N and not visited[di][dj]:
#                 queue.append([di, dj])
#                 if graph[v[0]][v[1]] == graph[di][dj]:
#                     visited[di][dj] = visited[v[0]][v[1]]
#                 else:
#                     num += 1
#                     visited[di][dj] = num
#     return visited, num


def bfs(graph, start, visited, num):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start[0]][start[1]] = num

    # 상 하 좌 우 [i + di, j + dj]
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    # 큐가 빌 때까지 탐색함
    while queue:
        v = queue.popleft()
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입함
        for d in directions:
            di = v[0] + d[0]
            dj = v[1] + d[1]
            if 0 <= di < N and 0 <= dj < N and not visited[di][dj]:
                if graph[v[0]][v[1]] == graph[di][dj]:
                    queue.append([di, dj])
                    visited[di][dj] = visited[v[0]][v[1]]
                
                if (graph[v[0]][v[1]] == 'R' and graph[di][dj] == 'G')\
                    or (graph[v[0]][v[1]] == 'G' and graph[di][dj] == 'R'):
                    queue.append([di, dj])
                    
    return visited


def bfs_as_same(graph, start, visited, num):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드 방문 처리
    visited[start[0]][start[1]] = num

    # 상 하 좌 우 [i + di, j + dj]
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    
    # 큐가 빌 때까지 탐색함
    while queue:
        v = queue.popleft()
        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입함
        for d in directions:
            di = v[0] + d[0]
            dj = v[1] + d[1]
            if 0 <= di < N and 0 <= dj < N and not visited[di][dj]:
                if graph[v[0]][v[1]] == graph[di][dj]:
                    queue.append([di, dj])
                    visited[di][dj] = visited[v[0]][v[1]]
                
                if (graph[v[0]][v[1]] == 'R' and graph[di][dj] == 'G')\
                    or (graph[v[0]][v[1]] == 'G' and graph[di][dj] == 'R'):
                    queue.append([di, dj])
                    visited[di][dj] = visited[v[0]][v[1]]

    return visited
                    

N = int(input())

painting = []
for _ in range(N):
    painting.append(list(input()))

visited1 = [[0] * N for _ in range(N)]
visited2 = [[0] * N for _ in range(N)]
num1 = num2 =  1

for i in range(N):
    for j in range(N):
        if not visited1[i][j]:
            visited1 = bfs(painting, [i, j], visited1, num1)
            num1 += 1
        
        if not visited2[i][j]:
            visited2 = bfs_as_same(painting, [i, j], visited2, num2)
            num2 += 1


print(visited1)
print(num1)
print()
print(visited2)
print(num2)