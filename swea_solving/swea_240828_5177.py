# SWEA 24.08.28.(수) - 5177.[파이썬 S/W 문제해결 기본] 8일차 - 이진 힙 (D2)
# 이진 최소힙: 완전 이진 트리를 유지하고자 마지막 노드 뒤에 새 노드를 추가함
# 1000000 이하인 N개의 서로 다른 자연수에 대해 입력 순서대로 이진 최소힙에 저장하고,
# 마지막 노드의 조상 노드에 저장된 정수의 합을 알아내는 프로그램을 작성하라

import sys
sys.stdin = open('sample_input\sample_input(42).txt', 'r')

# 최소힙
def enq(n):
    global last
    global heap

    last += 1

    # 마지막 노드에 데이터 삽입
    heap[last] = n
    
    # 부모 < 자식 비교를 위해
    child = last
    # 부모 번호 계산
    parent = child // 2

    # 부모가 있는데 값이 더 크면
    while parent > 0 and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]     # 교환함
        child = parent
        parent = child // 2    
    

T = int(input())

for tc in range(1, T + 1):
    # N: 입력되는 값의 개수
    N = int(input())
    inputs = list(map(int, input().split()))

    # 마지막 노드의 위치를 나타내는 인덱스
    last = 0
    result = 0              # 결과 값 저장 변수

    heap = [0] * (N + 1)    # 최소 힙

    # 힙에 값을 입력해줌
    for i in inputs:
        enq(i)

    # 마지막 노드의 조상 노드의 합 구하기
    while last != 0:
        last //= 2
        result += heap[last]

    print(f'#{tc} {result}')
        