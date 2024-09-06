# SWEA 24.09.06.(금) - 2819. 격자판의 숫자 이어붙이기 (D4)
# 4X4의 격자판의 각 격자칸에는 0~9 사이의 숫자가 적혀있다.
# 격자판의 임의의 위치에서 상하좌우 4방향으로 인접한 격자로 총 6번 이동하면서, 각 칸에 적힌 숫자를 차례로 이어붙이면 7자리의 수가 된다.
# 격자판이 주어질 때, 만들 수 있는 서로 다른 7자리 수들의 개수를 구하라.
# 단, 이동 시 한번 거쳤던 격자칸을 다시 거쳐도 되며, 0으로 시작하는 7자리 수를 만들어도 된다.

import sys
sys.stdin = open('sample_input\sample_input(61).txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    matrix = [list(map(int, input().split())) for _ in range(4)]

    