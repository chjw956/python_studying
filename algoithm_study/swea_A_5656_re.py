# SWEA [A형 대비 1] 5656. 벽돌 깨기
# 구슬을 쏘아 벽돌을 깨트리는 게임이다. 
# 구슬은 N번만 쏠 수 있고, 벽돌들은 W x H 배열로 주어진다.
# 벽돌은 1 ~ 9의 수로 표현되며, 0은 비어있는 지점을 의미한다.
# 구슬이 명중한 벽돌은 상하좌우 (벽돌에 적힌 숫자 - 1)칸 만큼의 벽돌이 같이 제거된다.
# 또한 벽돌 사이에 빈 공간이 생기는 경우, 벽돌은 중력에 의해 밑으로 내려가게 된다.
# N개의 벽돌을 떨어트려 최대한 많은 벽돌을 제거하려 할 때, 남은 벽돌의 개수를 구하라.
# 상웅 팁: 순열로 완전 탐색하여 풀이하라!

# 1열부터 W열까지 구슬을 칠 열을 순열로 생성

import sys
sys.stdin = open('sample_input\sample_input(4).txt', 'r')


# 백트래킹 활용 순열
def backtrack_perm(empty, length):
    global permutations
    if len(empty) == length:
        permutations.append(empty)
        return empty

    for i in range(len(array)):
        if used[i] == False:
            used[i] = True
            backtrack_perm(empty + [array[i]], length)
            used[i] = False


# 주어진 맵에서 해당 열의 시작 행을 찾아 반환
def findRow(matrix, col, h):
    for i in range(h):
        if matrix[i][col] != 0:
            return i


# 상 하 좌 우
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]


T = int(input())

for tc in range(1, T + 1):
    # N: 구슬을 쏘는 횟수, W x H: 주어진 배열의 크기
    N, W, H = map(int, input().split())
    block_map = [list(map(int, input().split())) for _ in range(H)]
    
    # 열 넘버를 array로 미리 생성
    array = list(i for i in range(0, W))
    used = [False for _ in range(len(array))]
    
    # 열 넘버로 순열을 만들어 저장
    permutations = []
    backtrack_perm([], N)

    # 만들어진 순열에 대해 남는 벽돌의 수가 가장 적은 것을 찾음
    for p in permutations:
        for c in p:
            # 해당 열의 가장 위쪽에 존재하는 벽돌의 위치 인덱스를 찾음
            r = findRow(block_map, c, H)
            # 해당 인덱스 벽돌의 값을 power로 설정
            power = block_map[r][c] - 1
            # 현재 블럭을 깨고
            block_map[r][c] = 0
            while power != 0:
                for [di, dj] in directions:
                    mi = r + di
                    mj = c + dj
                    # 만약 벽돌 지도 범위 안에 있고 빈 공간이 아닌 경우
                    if 0 <= mi < H and 0 <= mj < W and block_map[mi][mj] != 0:
                        # 현재 파워보다 큰 경우 파워 값 변경해줌 -> 이게 맞나..?
                        if block_map[mi][mj] - 1 > power:
                            power = block_map[mi][mj]



