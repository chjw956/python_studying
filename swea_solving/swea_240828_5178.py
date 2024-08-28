# SWEA 24.08.28.(수) 5178. [파이썬 S/W 문제해결 기본] 8일차 - 노드의 합 (D3)
# 리프 노드에 저장된 값에 대해 나머지 노드는 자식 노드의 합을 저장한다.
# 리프 노드의 번호와 저장된 값이 주어질 때, 지정한 노드 번호에 저장된 값을 출력하라.


import sys
sys.stdin = open('sample_input\sample_input(43).txt', 'r')

def numOfLayer (n):
    layer = 0
    while n > 0:
        n //= 2
        layer += 1
    return layer


T = int(input())

for tc in range(1, T + 1):
    # N: 총 노드의 수, M: 리프 노드 개수, L: 출력할 노드 번호
    N, M, L = map(int, input().split())

    heap = [0] * (N + 1)
    layer = numOfLayer(N)

    for _ in range(M):
        num, value = map(int, input().split())
        heap[num] = value
    
    last = 2 ** (layer - 1) - 1

    while last != 0:
        if 2 * last <= N :
            heap[last] += heap[2 * last]
        if 2 * last + 1 <= N :
            heap[last] += heap[2 * last + 1]

        last -= 1

    print(f'#{tc} {heap[L]}')

    
