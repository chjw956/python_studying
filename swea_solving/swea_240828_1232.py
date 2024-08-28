# SWEA 24.08.28.(수) - 1232.[S/W 문제해결 기본] 9일차 - 사칙연산 (D4)
# 수식 트리 관련 문제 (완전 이진 트리가 아님!!!!!)
# 사칙연산(+, -, *, /)와 양의 정수로만 구성된 임의의 이진 트리에 대해
# 이를 계산한 결과를 출력하는 프로그램을 작성하라.

import sys
sys.stdin = open('sample_input\sample_input(44).txt', 'r')
import operator

operators = {'+': operator.add,
             '-': operator.sub,
             '*': operator.mul,
             '/': operator.truediv}

for tc in range(1, 11):
    # N: 정점의 개수
    N = int(input())

    binary_tree = [0] * (N + 1)
    l = [0] * (N + 1)
    r = [0] * (N + 1)
    last = N
    
    # 이진 트리 생성
    for _ in range(N):
        # num: 연산자가 입력될 정점의 번호
        # oper: 연산자
        # value: 정점에 넣을 값
        inputs = list(input().split())
        num = int(inputs[0])
        if len(inputs) > 3:    
            oper = inputs[1]
            binary_tree[num] = oper
            l[num] = int(inputs[2])
            r[num] = int(inputs[3])
        else:
            value = int(inputs[1])
            binary_tree[num] = value

    # 마지막 정점이 우측 자식일 때,
    while last > 0:
        # 자식 노드가 존재할 때,
        if l[last] and r[last]:
            ope = operators[binary_tree[last]]
            binary_tree[last] = ope(binary_tree[l[last]], binary_tree[r[last]])
        last -= 1

    print(f'#{tc} {int(binary_tree[1])}')