# SWEA 24.09.13.(금) - 20551. 증가하는 사탕 수열 (D3)
# Python 3초, Java 2초
# 세 개의 상자가 나란히 존재할 때 각각 사탕 A, B, C개가 들어있다.
# 모든 상자는 비어있지 않고 각 상자에 있는 사탕의 개수가 순증가하도록 하려고 할 때,
# 이 조건을 만족시킬 수 있는지를 판단하고, 조건을 만족시키려면 몇 개의 사탕을 먹어 없애야 하는지 구하라.

import sys
sys.stdin = open('..\sample_input\sample_input(13).txt', 'r')


# 순증가로 구현 가능한지 확인
def crescendo(a, b, c):
    if c < 3 or b < 2:
        return False
    if a < 1:
        return False
    return True


T = int(input())

for tc in range(1, T + 1):
    a, b, c = map(int, input().split())
    result = -1
    # 1. 순증가하는 게 가능한지 확인
    check = crescendo(a, b, c)

    # 2-1. 가능하다면 몇 개의 사탕을 먹어 없앨지 확인
    # 2-2. 불가능하다면 -1 출력 후 continue
    if check:
        result = 0
        if b >= c:
            result += b - c + 1
            b = c - 1
        if a >= b:
            result += a - b + 1
            a = b - 1
    print(f'#{tc} {result}')