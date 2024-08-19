# DFS
# 백준 4963번 섬의 개수(silver 2)
import sys
sys.setrecursionlimit(10**6)                # 코테에서 이걸 써도 되는지 모르겠음

# DFS 메서드
def dfs(map_grid, sx, sy, visited, value):
    global w, h

    # 현재 노드 방문 처리
    visited[sy][sx] = value

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in range(-1, 2):
        for j in range(-1, 2):
            dx = sx + j
            dy = sy + i
            
            if 0 <= dx < w and 0 <= dy < h and map_grid[dy][dx] == 1:
                if not visited[dy][dx]:
                    # visited[dy][dx] = value
                    map_grid[dy][dx] = 0
                    dfs(map_grid, dx, dy, visited, value)


# 입력된 지도에서 임의의 출발점 잡기
def findNotVisited(map_grid, w, h):
    for i in range(h):
        for j in range(w):
            if map_grid[i][j] == 1:
                sy, sx = i, j
                return sy, sx
    return -1, -1


while True:
    w, h = map(int, input().split())            # w: 지도의 너비, h: 지도의 높이

    if w == 0 and h == 0:
        break
    else:
        # 지도 생성        
        map_grid = []
        for _ in range(h):
            map_grid.append(list(map(int, input().split())))
        
        visited = [[0 for _ in range(w)] for __ in range(h)]

        sx = sy = 0
        value = 1

        while sx != -1 and sy != -1:
            # 출발점 구하기
            sy, sx = findNotVisited(map_grid, w, h)
            
            if sx == sy == -1:
                break
            
            map_grid[sy][sx] = 0

            dfs(map_grid, sx, sy, visited, value)

            value += 1

        print(value - 1)