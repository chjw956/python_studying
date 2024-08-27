# SWEA 24.08.27.(화) - 5174. [파이썬 S/W 문제해결 기본] 8일차 - subtree
# 주어진 이진 트리에서 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수를 알아내는 프로그램을 만드시오.
# 주어지는 트리는 부모가 없는 노드가 전체의 루트 노드가 된다.

import sys
sys.stdin = open('sample_input\sample_input(40).txt', 'r')

def countChild(left, right, root):
    global cnt

    if left[root] == 0 and right[root] == 0:
        return
    
    if left[root]:
        cnt += 1
        countChild(left, right, left[root])
    if right[root]:
        cnt += 1
        countChild(left, right, right[root])


T = int(input())

for tc in range(1, T + 1):
    # E: 간선의 개수, N: 루트 노드의 값
    E, N = map(int, input().split())
    edges = list(map(int, input().split()))

    left = [0] * (E + 2)
    right = [0] * (E + 2)

    for i in range(0, len(edges), 2):
        parent, child = edges[i], edges[i + 1]

        if not left[parent]:
            left[parent] = child
        elif not right[parent]:
            right[parent] = child

    # 노드 N을 루트로 하는 서브 트리에 속한 노드의 개수
    cnt = 1
     
    countChild(left, right, N)

    print(f'#{tc} {cnt}')