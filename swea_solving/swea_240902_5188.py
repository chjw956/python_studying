# SWEA 24.09.02.(월) 5188. 최소합(D3)
# NxN 칸에 숫자가 적힌 판이 있을 때, 각 칸에서는 오른쪽이나 아래로만 이동할 수 있다.
# 맨 왼쪽 위에서 오른쪽 아래까지 이동할 때, 지나는 칸에 써진 숫자의 합계가 최소가 되는 값을 출력하라.

import sys
sys.stdin = open('sample_input\sample_input(53).txt', 'r')


def solve(si, sj, rslt):
    global min_rslt

    if si == N - 1 and sj == N - 1:
        min_rslt = min(rslt, min_rslt)
        return
    
    for di, dj in direction:
        mi = si + di
        mj = sj + dj

        if mi < N and mj < N:
            rslt += matrix[mi][mj]
            solve(mi, mj, rslt)
            rslt -= matrix[mi][mj]


# 진행 가능 방향: 오른쪽, 아래
direction = [[0, 1], [1, 0]]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())            # N: 가로 세로 칸 수
    matrix = [list(map(int, input().split())) for _ in range(N)]

    min_rslt = 10000

    solve(0, 0, matrix[0][0])

    print(f'#{tc} {min_rslt}')