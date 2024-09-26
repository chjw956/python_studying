# 백준 11048. 이동하기 (silver 2) - DP
# NxM 크기의 미로에서 (1, 1)에서 (N, M)으로 이동하면서 각 방의 사탕을 가져간다고 할 때,
# 준규가 가져올 수 있는 사탕의 최대 개수를 구하라.
# (단, 이동 방향은 오른쪽, 아래쪽, 대각선 오른쪽 아래 방향으로만 가능하다.)

import sys
sys.stdin = open('sample_input\sample_input(21).txt', 'r')

directions = [[1, 0], [0, 1], [1, 1]]

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    miro = [[0] * (M + 1)]

    for _ in range(N):
        miro.append([0] + list(map(int, input().split())))

    # 이전 값을 저장할 dp 테이블 생성
    d = [[0] * (M + 1) for _ in range(N + 1)]

    # 출발점
    si = sj = 1
    d[si][sj] = miro[si][sj]

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            d[i][j] = max(d[i-1][j], d[i][j-1], d[i-1][j-1]) + miro[i][j]

    print(d[N][M])