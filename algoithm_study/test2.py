from collections import deque
from itertools import combinations

# 상하좌우 방향
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]


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

# 입력 처리
matrix = [list(input().strip()) for _ in range(5)]

# 5x5 격자의 모든 좌표 생성
coordinates = [(i, j) for i in range(5) for j in range(5)]

result = 0  # 가능한 조합의 수

# 1. 모든 조합 생성 (7명을 선택)
for comb in combinations(coordinates, 7):
    # 2. 선택된 조합에서 '이다솜파(S)' 학생 수 세기
    s_count = sum(1 for x, y in comb if matrix[x][y] == 'S')
    
    # '이다솜파'가 4명 이상인 경우만 인접성 검사 진행
    if s_count >= 4 and bfs(comb):
        result += 1

# 가능한 조합의 수 출력
print(result)