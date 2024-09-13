# SWEA 24.09.05.(목) - 5208. 전기버스2 (D3)
# Java, Python 2초
# 전기버스 정류장에는 충전지마다 최대 운행 가능한 정류장 수가 정해져 있다.
# 충전지가 방전되기 전에 교체하여 운영해야 할 때, 목적지에 도달하기 위한 최소한의 교체 횟수는 얼마인가?
# import sys
# sys.stdin = open('..\sample_input\sample_input(15).txt', 'r')


# 부분집합 생성
def makeSubset(s):
    for b in range(s + 1, N - 1):
        size = len(stopBy)
        for i in range(size):
            stopBy.append(stopBy[i] + [[b, battery[b]]])


T = int(input())

for tc in range(1, T + 1):
    N, *battery = map(int, input().split())
    must = [[0, battery[0]]]

    stopBy = [must]

    num = N - 1

    # 1. 부분집합 생성
    makeSubset(must[-1][0])

    # 2. 완전 탐색을 통해 부분집합의 length가 가장 작은 것 선택
    for stop in stopBy:
        # 마지막으로 충전한 양이 도착지까지 도달할 수 없는 양인 경우 -> 불가능한 케이스
        if stop[-1][1] < (N - 1) - stop[-1][0]:
            continue

        possible = True

        for i in range(1, len(stop)):
            # 선택된 충전지 이전에 충전한 값이 이전 충전지부터 현재 충전지까지 거리보다 작은 경우
            if stop[i - 1][1] < stop[i][0] - stop[i - 1][0]:
                possible = False
                break
        if not possible:
            continue

        # 가능한 케이스로 걸러진 것들 중에 가장 길이가 짧은 것을 선택
        if num > len(stop):
            num = len(stop)

    print(f'#{tc} {num - 1}')