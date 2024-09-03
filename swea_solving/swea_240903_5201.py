# SWEA 24.09.03.(화) - 컨테이너 운반 (D3)
# 화물이 실려 있는 N개의 컨테이너를 M대의 트럭으로 A도시에서 B도시로 편도로 운반할 때,
# 트럭 당 한 개의 컨테이너를 운반할 수 있고, 트럭의 적재용량을 초과하면 안된다.
# 컨테이너마다 실린 화물의 무게와 트럭마다의 적재용량이 주어질 때, 
# 이동한 화물의 총 중량이 최대가 되도록 컨테이너를 옮겼다면, 옮겨진 화물의 전체 무게가 얼마인지 출력하라.
# 컨테이너를 하나도 옮길 수 없는 경우 0을 출력한다.

import sys
sys.stdin = open('sample_input\sample_input(52).txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    # N: 컨테이너 수, M: 트럭 수
    N, M = map(int, input().split())
    weights = list(map(int, input().split()))       # N개의 화물의 무게
    limits = list(map(int, input().split()))        # M개 트럭의 각각의 적재 용량

    container = 0           # 옮긴 컨테이너의 무게

    # 화물과 트럭을 무거운 순서로 정렬
    weights.sort(reverse = True)        
    limits.sort(reverse = True)

    for i in range(M):
        for j in range(N):
            if weights[j] == 0:
                continue
            if limits[i] >= weights[j]:
                limits[i] -= weights[j]
                container += weights[j]
                weights[j] = 0
                break
                 
    print(f'#{tc} {container}')