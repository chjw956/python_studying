# 백준 17136. 색종이 붙이기 (G2)
# 5종류(1x1, 2x2, 3x3, 4x4, 5x5)의 색종이를 각각 5장씩 가지고 있다고 할 때, 이것을 10x10 크기의 종이 위에 붙이려고 한다.
# 종이가 주어질 때, 1이 적힌 모든 칸을 붙이는 데 필요한 색종이의 최소 개수를 구하라.
# (0이 적힌 칸에는 색종이를 붙일 수 없으며, 1을 모두 덮는 것이 불가능한 경우에는 -1을 출력한다.)

import sys
sys.stdin = open('sample_input\sample_input(10).txt', 'r')


for _ in range(8):
    tc = int(input())
    paper = [list(map(int, input().split)) for _ in range(10)]
    result = -1
