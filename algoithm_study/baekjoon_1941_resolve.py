# 백준 1941. 소문난 칠공주(gold3)
# 5x5의 정사각 격자 형태로 구성된 반 배치에서
# 7명의 여학생들에 대해 위치는 가로나 세로로 반드시 인접해 있어야 하며,
# '이다솜파' 학생들로만 구성될 필요는 없으나 최소 4명 이상이 이다솜파여야 한다.
# 7명의 여학생을 구성할 수 있는 경우의 수를 구하라.
# 시간 제한: 2초
from collections import deque


# 조합(재귀)
def combination(lev, start):
    global temp_princesses
    
    if lev == 7:
        temp_princesses.append(group[:])
        return

    for i in range(start, len(coordinates)):
        if coordinates[i] not in group:
            group.append(coordinates[i])
            combination(lev + 1, i + 1)
            group.pop()


# BFS
def bfs(si, sj):
    global temp
    
    visited[si][sj] = 1

    q = deque([[si, sj]])

    while q:
        vi, vj = q.popleft()
        
        for di, dj in directions:
            ni = vi + di
            nj = vj + dj
            # 교실 범위 내에 위치하고
            if 0 <= ni < 5 and 0 <= nj < 5 and not visited[ni][nj]:
                visited[ni][nj] = visited[vi][vj] + 1
                q.append([ni, nj])


matrix = [list(input()) for _ in range(5)]
coordinates = []
for i in range(5):
    for j in range(5):
        coordinates.append([i, j])

group = []
temp_princesses = []        # 임시 칠공주 리스트 모음
seven_princesses = []       # 최종적으로 가능한 칠공주 조합

# 상하좌우
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# 1. 7명의 학생 조합을 구함
combination(0, 0)

# 2. 구한 조합에 대해 4명의 이다솜파가 있는지 and 연결되어 있는지 확인
for temp in temp_princesses:
    # print(f'temp = {temp}')
    # 2-1. 4명의 이다솜파가 있는지 확인
    cnt = 0
    for [ti, tj] in temp:
        if matrix[ti][tj] == 'S':
            cnt += 1
    if cnt < 4:
        continue

    # 2-2. 연결되어 있는지 확인
    visited = list([0] * 5 for _ in range(5))   # BFS에 사용
    bfs(temp[0][0], temp[0][1])

    flag = False
    cnt = 0

    # 2-2-1. 7이내의 수들로 채워져있는지 확인
    for n in range(len(temp)):
        if visited[temp[n][0]][temp[n][1]] > 7:
            break
    
        # 2-2-2. temp 내의 점들과 연결되는지 확인
        for di, dj in directions:
            ni = temp[n][0] + di
            nj = temp[n][1] + dj
            if 0 <= ni < 5 and 0 <= nj < 5 and ([ni, nj] in temp):     
                print(temp[n], f'[ni, nj] = [{ni}, {nj}]')
                flag = True
                break
        
        if flag:
            cnt += 1

    if cnt == 7:
        seven_princesses.append(temp)

for s in seven_princesses:
    print(s)
print(len(seven_princesses))