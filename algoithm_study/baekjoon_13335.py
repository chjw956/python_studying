# 백준 13335. 트럭(silver 1)
# 강 위의 다리를 n개의 트럭이 건너려고 한다.
# 다리 위에는 w대의 트럭만이 동시에 올라갈 수 있다고 할 때, 
# 모든 트럭들이 다리를 건너는 최단 시간을 출력하라.
# 단, 트럭의 순서는 변경할 수 없으며 트럭의 무게는 서로 같지 않을 수 있다.
# 시간 제한 1초

import sys
sys.stdin = open('sample_input\sample_input(23).txt.', 'r')

T = int(input())

for tc in range(1, T + 1):
    # n: 트럭의 수, w: 다리 길이, L: 다리의 최대 하중
    n, w, L = map(int, input().split())
    weights = [0]
    weights += [i for i in map(int, input().split())]