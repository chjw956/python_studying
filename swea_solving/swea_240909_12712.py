# SWEA 24.09.09.(월) - 12712. 파리퇴치3 (D2)
# N x N 배열이 주어질 때, 각 칸의 숫자는 해당 영역에 있는 파리 개체 수를 나타낸다.
# 파리 킬러 스프레이를 뿌려 최대한 많은 파리를 잡으려고 하는데, 스프레이는 + 혹은 x 형태로 분사된다.
# 스프레이를 M의 세기로 분사하면 노즐의 중심 칸을 포함하여 각 방향으로 M칸의 파리를 잡을 수 있다.
# 한 번에 잡을 수 있는 최대 파리수를 출력하라.

import sys
sys.stdin = open('sample_input\sample_input(64).txt', 'r')

# + 형태
plus_drct = [[-1, 0], [1, 0], [0, -1], [0, 1]]

# x 형태
mult_drct = [[-1, -1], [-1, 1], [1, -1], [1, 1]]

T = int(input())

for tc in range(1, T + 1):
    # N: 배열의 크기, M: 스프레이의 세기
    N, M = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_flies = flies = 0

    for i in range(N):
        for j in range(N):
            flies = matrix[i][j]
            fly = 0
            for [pi, pj] in plus_drct:
                for k in range(1, M):
                    ni = i + pi * k
                    nj = j + pj * k
                
                    if 0 <= ni < N and 0 <= nj < N:
                        fly += matrix[ni][nj]
            max_flies = max(max_flies, flies + fly)
            fly = 0
            for [mi, mj] in mult_drct:
                for k in range(1, M):
                    ni = i + mi * k
                    nj = j + mj * k
                
                    if 0 <= ni < N and 0 <= nj < N:
                        fly += matrix[ni][nj]
            max_flies = max(max_flies, flies + fly)
    
    print(f'#{tc} {max_flies}')