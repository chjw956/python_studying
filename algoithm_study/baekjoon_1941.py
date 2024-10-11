# 백준 1941. 소문난 칠공주(gold3)
# 5x5의 정사각 격자 형태로 구성된 반 배치에서
# 7명의 여학생들에 대해 위치는 가로나 세로로 반드시 인접해 있어야 하며,
# '이다솜파' 학생들로만 구성될 필요는 없으나 최소 4명 이상이 이다솜파여야 한다.
# 7명의 여학생을 구성할 수 있는 경우의 수를 구하라.
# 시간 제한: 2초

from collections import deque


def isPossible(lst):
    dist = 0
    lst.sort(key=lambda x:x[0])     # 행 정보를 기준으로 정렬
    for k in range(1, len(lst)):
        if lst[k][0] == lst[k -1][0]:
            dist += abs(lst[k][1] - lst[k - 1][1])
        else:
            dist += abs(lst[k][0] - lst[k - 1][0])
    return dist


# 조합(재귀)
def combination(lev, start):
    global temp_princesses

    # if 4 <= lev <= 7:
    if lev == 4:
        if isPossible(group) < 7:
            temp_princesses.append(group[:])
        return
    
    for i in range(start, len(lds)):
        group.append(lds[i])
        combination(lev + 1, i + 1)
        group.pop()


def bfs(si, sj, gi, gj):
    global temp
    
    q = deque([[si, sj]])

    while q:
        vi, vj = q.popleft()
        
        if vi == gi and vj == gj:
            return visited[vi][vj]
        
        for di, dj in directions:
            ni = vi + di
            nj = vj + dj
            # 교실 범위 내에 위치하고
            if 0 <= ni < 5 and 0 <= nj < 5 and not visited[ni][nj]:
                visited[ni][nj] = visited[vi][vj] + 1
                q.append([ni, nj])


matrix = [list(input()) for _ in range(5)]

lds = []                    # 이다솜파 학생들의 좌표 모음
group = []                  # 조합 그룹 임시 저장
temp_princesses = []        # 미완성 칠공주 리스트 모음
seven_princesses = []       # 최종적으로 가능한 칠공주 조합

directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# 1. 이다솜파 학생들의 좌표를 모두 구함
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 'S':
            lds += [[i, j]]

# 2. 이다솜파 학생들로 4명의 조합을 모두 구한다.
combination(0, 0)

# print(f'temp_princesses = {temp_princesses}')

# 3. 만들어진 조합에 대해 나머지 인원을 추가함으로써 모두가 연결될 수 있는지 확인한다.
for temp in temp_princesses:
    flag = True
    visited = list([0] * 5 for _ in range(5))   # BFS에 사용
    visited[temp[0][0]][temp[0][1]] = 1         # 시작점 방문 표시

    for k in range(1, len(temp)):
        bfs(temp[k - 1][0], temp[k - 1][1], temp[k][0], temp[k][1])

    for ti, tj in temp:
        if visited[ti][tj] == 0:
            values = []
            for di, dj in directions:
                ni = temp[-1][0] + di
                nj = temp[-1][1] + dj
                if 0 <= ni < 5 and 0 <= nj < 5 and visited[ni][nj]:
                    values.append(visited[ni][nj])
            if values:
                visited[ti][tj] = min(values) + 1
        elif visited[ti][tj] > 7:
            flag = False

    if flag:
        if temp not in seven_princesses:
            seven_princesses.append(temp)

print(len(seven_princesses))