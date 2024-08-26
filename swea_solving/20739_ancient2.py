# 24.08.26.(월) SWEA 20739. 고대 유적 2 (D2)
# 땅 속에서 N X N의 고대 구조물이 발견되었다.
# 구조물에서 구조물이 있는 자리는 1, 빈 곳은 0으로 표시된다.
# 구조물의 최소 크기는 1 X 2m이므로 만약 1칸만 1로 표시된 곳은 사진의 노이즈가 생긴 것이다.
# 또한 구조물은 직선인 구조로, 서로 다른 깊이에 묻혀있으므로 교차하거나 만나는 것처럼 보이는 구조물은 하나의 구조물이 아니다.
# 각 테스트케이스 별로 가장 긴 구조물의 길이를 출력하고, 만약 구조물이 하나도 없는 경우 0을 출력한다.

# 내가 생각한 로직

import sys
sys.stdin = open('sample_input\sample_input(38).txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    matrix = [list(map(int, input().split())) for _ in range(N)]