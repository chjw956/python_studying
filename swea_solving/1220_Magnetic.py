# 24.08.26.(월) SWEA 1220.Magnetic (D2)
# 테이블 위에 놓인 자성체들이 일정 간격을 두고 놓여있다. 강한 자기장을 걸었을 때, 
# 테이블 위에 자성체들이 충돌하여 남아있는 교착 상태의 개수를 구하라.
# 1은 N극 성질, 2는 S극 성질
# 테이블의 윗부분이 N극, 아랫 부분이 S극이다.

# 열마다 순환하면서 행 별로아래로 이동하는 N극 자성체가 존재하는 경우,
# 마지막 행이 될 때까지 S극 자성체가 존재하면 교착 상태에 빠지는 것으로 간주하고
# 카운팅하는 방법으로 로직 작성하기!

import sys
sys.stdin = open('sample_input\sample_input(35).txt', 'r')


for tc in range(1, 11):
    N= int(input())            # N = 100

    table = [list(map(int, input().split())) for _ in range(N)]

    print(table)