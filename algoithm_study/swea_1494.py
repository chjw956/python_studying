# SWEA 1494.사랑의 카운슬러 (D4)
# 지렁이가 N마리 있을 때, 지렁이 2마리를 매칭시키고자 한다.
# 모든 지렁이들을 매칭시키되, 각 지렁이들이 움직인 벡터의 크기를 합하여 최소가 되도록 하라.

import sys
sys.stdin = open('sample_input\sample_input(9).txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    # N: 지렁이 마리 수
    N = int(input())