# 백준 3190. 뱀 (gold 4)
# 사과를 먹으면 몸 길이가 늘어나는 뱀이 N x N 보드 위에서 이동할 때, 벽이나 자기자신의 몸과 부딪히면 게임이 종료된다.
# 게임 시작 시 뱀은 맨위 맨좌측에 위치하며 몸 길이는 1이다. 또한 보드의 상하좌우 끝에 벽이 있다고 한다.
# 뱀은 처음에 오른쪽을 향하며, 몸 길이가 늘어날 땐 꼬리는 그대로 있고 머리가 한 칸 자라나 앞으로 이동한다.
# 사과의 위치와 뱀의 이동경로가 주어질 때, 이 게임이 몇 초에 끝나는지 계산하라.

import sys
sys.stdin = open('sample_input\sample_input(24).txt', 'r')
from collections import deque


T = int(input())

for tc in range(1, T + 1):
    N = int(input())            # 보드 크기
    K = int(input())            # 사과 개수
    apples = [list(map(int, input().split())) for _ in range(K)]

    L = int(input())            # 방향 전환 횟수
    move = [list(input().split()) for _ in range(L)]     # L: 왼쪽, D: 오른쪽

    driving = [0] * (N * N)

    for [i, j] in move:
        driving[int(i)] = j

    ni = nj = 0                     # 뱀 머리의 현재 위치
    heading = [0, 1]                # 위치가 아닌 방향을 나타냄
    snake = deque([[0, 0]])
    for s in range(len(driving)):
        # 방향 전환(우)
        if driving[s] == 'D':
            # 좌우 방향 이동중이었던 경우
            if heading[0] == 0 and heading[1] != 0:
                heading[0] = heading[1]
                heading[1] = 0
            # 상하 방향 이동중이었던 경우
            elif heading[0] != 0 and heading[1] == 0:
                heading[1] = -heading[0]
                heading[0] = 0
        # 방향 전환(좌)
        elif driving[s] == 'L':
            # 좌우 방향 이동중이었던 경우
            if heading[0] == 0 and heading[1] != 0:
                heading[0] = -heading[1]
                heading[1] = 0
            # 상하 방향 이동중이었던 경우
            elif heading[0] != 0 and heading[1] == 0:
                heading[1] = heading[0]
                heading[0] = 0

        # 뱀 머리의 현재 위치
        ni += heading[0]
        nj += heading[1]
        
        # 벽에 부딪히지 않고, 몸에 부딪히지 않는다면
        if 0 <= ni < N and 0 <= nj < N and ([ni, nj] not in snake):
            # 사과가 존재하지 않는 칸이라면
            if [ni + 1, nj + 1] not in apples:
                snake.append([ni, nj])
                snake.popleft()         # 꼬리가 위치한 칸을 비워줌
            # 사과가 존재하는 칸이라면
            else:
                snake.append([ni, nj])
        # 벽 또는 몸에 부딪힌 경우
        else:
            print(s + 1)
            break