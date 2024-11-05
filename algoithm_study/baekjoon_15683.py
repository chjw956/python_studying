# 백준 15683. 감시 (gold 3)
# 5 종류의 CCTV가 존재할 때, 주어진 지도에서 0은 빈 칸, 6은 벽, 1~5는 CCTV 번호를 의미한다.
# CCTV는 감시할 수 있는 방향의 모든 칸을 감시할 수 있으나 벽은 통과하지 못한다.
# 단 CCTV는 CCTV를 통과할 수 있다.
# k개의 CCTV가 설치되어 있다고 할 때, CCTV의 방향을 적절히 조절하여 사각지대의 최소 크기를 구하여라.
# 단 0 <= k <= 8 이며, CCTV는 90도 방향으로만 회전이 가능하다.
# 시간 제한 1초

# 백트래킹으로 하려고 했는데, 굳이 matrix에 표기된 정보를 변경하고 백트래킹하는 과정을 포함해야 하는지에 대해
# 의문이 생겨서 set으로 구현함

import sys
sys.stdin = open('sample_input\sample_input(26).txt', 'r')

# 상 우 하 좌
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]

cctvs = {
    1 : [[1], [2], [3], [0]],
    2 : [[1, 3], [0, 2]],
    3 : [[0, 1], [1, 2], [2, 3], [3, 0]],
    4 : [[3, 0, 1], [0, 1, 2], [1, 2, 3], [2, 3, 0]],
    5 : [[0, 1, 2, 3]]
}

# 완전탐색(백트래킹 - dfs)
def solution(depth, watched):
    global min_blinded, wall, N, M
    
    # 백트래킹 탈출 조건 : 모든 CCTV 방향 설정 완료
    # 사각지대 계산
    if depth == len(cctv):
        min_blinded = min(min_blinded, N * M - (wall + len(cctv) + len(watched)))
        return
    
    # 현재 CCTV 좌표 정보
    ci, cj = cctv[depth]
    cctv_type = matrix[ci][cj]

    for direction in cctvs[cctv_type]:
        through = set()        # 현재 CCTV의 각 방향에서 감시 가능한 좌표를 임시 저장할 set
        for d in direction:
            di, dj = directions[d]
            k = 1
            while True:
                ni = ci + di * k
                nj = cj + dj * k
                
                # 범위를 넘어가거나 벽인 경우 break
                if (ni < 0 or ni >= N or nj < 0 or nj >= M) or matrix[ni][nj] == 6:
                    break
                
                # 빈칸인 경우 감시
                if matrix[ni][nj] == 0:
                    through.add((ni, nj))
                k += 1              # 이거 중요함
    
        # 현재 CCTV가 감시한 영역을 포함하여 다음 CCTV로 이동
        solution(depth +1, watched | through)


T = int(input())            # 테스트 케이스 개수

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    wall = 0
    cctv = []    
    
    # CCTV와 벽 위치 모두 찾기
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if 1 <= matrix[i][j] <= 5:
                cctv.append((i, j))
            elif matrix[i][j] == 6:
                wall += 1
    
    min_blinded = N * M
    
    solution(0, set())
    print(f'#{tc} {min_blinded}')