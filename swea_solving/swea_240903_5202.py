# SWEA 24.09.03.(화) - 5202. [파이썬 S/W 문제해결 구현] 3일차 - 화물 토크 (D3)
# 0시부터 다음날 0시 이전까지 A 도크의 사용신청을 확인해 최대한 많은 화물차가 화물을 싣고 내릴 수 있도록 한다면,
# 최대 몇 대의 화물차가 이용할 수 있는지 출력하라.


import sys
sys.stdin = open('sample_input\sample_input(51).txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())            # N: 신청서의 개수
    apply = []
    cnt = 0

    for _ in range(N):
        s, e = map(int, input().split())
        apply.append((s, e))

    # 종료시간 기준 정렬
    apply.sort(key = lambda x:x[1], reverse = True)

    reservation = [apply[-1]]
    cnt += 1
    apply.pop()

    for i in range(len(apply) - 1, -1, -1):
        # 등록된 예약의 종료 시간 이후에 신청 시작 시간이 위치한다면,
        if apply[i][0] >= reservation[-1][1]:
            reservation.append(apply[i])
            cnt += 1

    print(f'#{tc} {cnt}')