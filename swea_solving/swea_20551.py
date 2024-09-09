# SWEA 24.09.09.(월) 20551. 증가하는 사탕 수열(D3)
# 세 개의 상자가 나란히 있을 때 각 상자에 사탕을 A개, B개, C개를 넣어두려 한다.
# 각 상자가 비어있지 않으면서 들어있는 사탕의 개수가 순증가하도록 하려고 할 때, 
# 이 조건을 맞추기 위해 넘치는 사탕을 세현이가 먹어 없앤다고 하면 최소 몇 개의 사탕을 먹어야 하는가?

import sys
sys.stdin = open('sample_input\sample_input(63).txt', 'r')

T = int(input())

# 내가 작성한 코드
for tc in range(1, T + 1):
    A, B, C = map(int, input().split())

    if C <= 2 or B <= 1:
        print(f'#{tc} -1')
        continue

    totalEat = toEat = 0

    if B >= C:
        toEat = B - C + 1
        B -= toEat
        totalEat += toEat
    
    if A >= B:
        toEat = A - B + 1
        A -= toEat
        totalEat += toEat

    print(f'#{tc} {totalEat}')



"""
# 라이브 강사님이 작성하신 코드
for tc in range(1, T + 1):
    A, B, C = map(int, input().split())

    # A < B < C 구조로 만들 수 없는 케이스를 처리함
    if B < 2 or C < 3:
        print(f'#{tc} -1')
        continue

    eat = 0

    if B >= C:
        eat += B - (C - 1)
        B = C - 1

    if A >= B:
        eat += A - (B - 1)
        A = B - 1

    print(f'#{tc} {eat}')

"""
