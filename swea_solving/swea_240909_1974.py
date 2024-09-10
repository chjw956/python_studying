# SWEA 24.09.09.(월) - 1974. 스도쿠 검증 (D2)
# 입력으로 9 x 9 크기의 스도쿠 퍼즐이 주어질 때, 스도쿠 규칙을 만족하면 1을 출력하고
# 그렇지 않을 경우 0을 출력한다.
# Python 30초, Java 30초

import sys
sys.stdin = open('sample_input\sample_input(65).txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    matrix = [list(map(int, input().split())) for _ in range(9)]
    rslt = 1

    # 대각선에 있는 점들만 검사
    for i in range(9):
        # 행 검사
        used = [False] * 9
        for k in range(9):
            if not used[matrix[i][k] - 1]:
                used[matrix[i][k] - 1] = True
            else:
                rslt = 0

        # 열 검사
        used = [False] * 9
        for k in range(9):
            if not used[matrix[k][i] - 1]:
                used[matrix[k][i] - 1] = True
            else:
                rslt = 0

    # 3x3 검사
    for i in range(0, 7, 3):
        used = [False] * 9
        for _ in range(2):
            if not used[matrix[i + 1][i] - 1]:
                used[matrix[i + 1][i] - 1] = True
            else:
                rslt = 0
            if not used[matrix[i][i + 1] - 1]:
                used[matrix[i][i + 1] - 1] = True
            else:
                rslt = 0
            if not used[matrix[i + 1][i + 1] - 1]:
                used[matrix[i + 1][i + 1] - 1] = True
            else:
                rslt = 0
            i += 1

    print(f'#{tc} {rslt}')