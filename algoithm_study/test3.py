from collections import deque

def bfs(selected):
    # 선택된 7명의 학생이 모두 인접해 있는지 BFS로 확인
    q = deque([selected[0]])        # 시작 좌표
    visited = set([selected[0]])    # 방문한 좌표 표시
    count = 1                       # 시작점 포함

    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if (nx, ny) in selected and (nx, ny) not in visited:
                visited.add((nx, ny))
                q.append((nx, ny))
                count += 1
                if count == 7:  # 7명 모두 연결되면 즉시 종료
                    return True
    return False                # 연결되지 않은 경우


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

result = 0  # 가능한 조합의 수

# 1. 7명의 학생 조합을 구함
combination(0, 0)

# 1. 모든 조합 생성 (7명을 선택)
for comb in temp_princesses:
    # 2. 선택된 조합에서 '이다솜파(S)' 학생 수 세기
    s_count = sum(1 for x, y in comb if matrix[x][y] == 'S')
    
    # '이다솜파'가 4명 이상인 경우만 인접성 검사 진행
    if s_count >= 4 and bfs(comb):
        result += 1

# 가능한 조합의 수 출력
print(result)