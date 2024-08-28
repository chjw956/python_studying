# SWEA A형 대비 1 1953. [모의 SW 역량테스트] 탈주범 검거
# 숫자 1 ~ 7은 해당 위치의 터널 구조물 타입을 의미
# 숫자 0은 터널이 없는 장소임을 나타냄

import sys
sys.stdin = open('sample_input\sample_input(5).txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())

    ternal = [list(map(int, input().split)) for _ in range(N)]
