# SWEA 24.09.05.(목) 5209. 최소 생산 비용 (D3)
# Python 2초
# N종의 제품을 N곳의 공장에서 한 곳당 한 가지씩 생산하고자 할 때,
# 각 제품의 공장별 생산비용이 주어질 때, 전체 제품의 최소 생산 비용을 계산하라.

import sys
sys.stdin = open('..\sample_input\sample_input(15).txt', 'r')


def permutation(empty, k):
    if len(empty) == k:
        return

    for n in range(N):
        pass


T = int(input())

for tc in range(1, T + 1):
    # N: 제품 개수 = 생산 공장 개수
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]