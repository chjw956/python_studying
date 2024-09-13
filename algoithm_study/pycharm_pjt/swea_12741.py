# SWEA 12741. 두 전구 (D3)
# Python 4초, Java 4초
# 두 전구 x, y에 대해 0초에서 100초 간 두 전구가 언제 켜지는지 관찰했을 때,
# x는 A초 ~ B초, y는 C초 ~ D초에 켜져있었다고 한다.
# 그렇다면 두 전구가 동시에 켜져 있던 시간은 몇 초인가?

import sys
sys.stdin = open('..\sample_input\sample_input(14).txt', 'r')

T = int(input())
result = []

for _ in range(T):
    A, B, C, D = map(int, input().split())
    total = 0
    start = end = 0

    # 겹치는 경우
    if B > C and D > A:
        if A <= C:
            start = C
        else:
            start = A

        if B <= D:
            end = B
        else:
            end = D

    total = end - start
    result.append(total)

for i, t in enumerate(result):
    print(f'#{i + 1} {t}')
