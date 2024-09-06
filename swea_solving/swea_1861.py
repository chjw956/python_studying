# SWEA 24.09.06.(금) - 1861. 정사각형 방 (D4)
# N^2 개의 방이 N x N 형태로 늘어서 있을 때, 각 방에는 숫자가 기입되어 있다.
# 출발점에서 상하좌우의 다른 방으로 이동 가능할 때, 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야 한다.
# 이때 처음 어떤 수가 적힌 방에 있어야 가장 많은 개수의 방을 이동할 수 있는지 구하라.

import sys
sys.stdin = open('sample_input\sample_input(59).txt', 'r')

# 강사님 로직 보고 작성한 코드
# 1. 1부터 N**2을 인덱스로 갖는 배열 A를 만듦
# 2. 숫자 i의 인접에 1 큰 수가 존재하는 경우 A[i]에 1을 표시함
# 3. 연속한 1의 개수가 최대인 경우를 찾음


# 상 하 좌 우
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]

    # 1부터 N^2까지를 인덱스로 갖는 배열 생성
    visited = [0] * (N ** 2 + 1)
    for i in range(N):
        for j in range(N):
            for d in directions:
                mi = i + d[0]
                mj = j + d[1]
                if 0 <= mi < N and 0 <= mj < N:
                    if rooms[mi][mj] - rooms[i][j] == 1:
                        visited[rooms[i][j]] = 1
                        break               # 하나라도 존재하는지만 확인

    mx_len = mx_room = 0
    length = start = 1

    # 1이 최대로 연속하는 길이를 찾음
    # 방에 적힌 값의 범위: 1 ~ N^2
    for k in range(1, N ** 2 + 1):
        if visited[k] == 1:
            length += 1
        else:
            if mx_len < length:
                mx_len = length
                mx_room = start
            start = k + 1
            length = 1

    print(f'#{tc} {mx_room} {mx_len}')