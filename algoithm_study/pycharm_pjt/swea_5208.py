# SWEA 24.09.05.(목) - 5208. 전기버스2 (D3)
# Java 2초
# 전기버스 정류장에는 충전지마다 최대 운행 가능한 정류장 수가 정해져 있다.
# 충전지가 방전되기 전에 교체하여 운영해야 할 때, 목적지에 도달하기 위한 최소한의 교체 횟수는 얼마인가?
# import sys
# sys.stdin = open('..\sample_input\sample_input(15).txt', 'r')


# 부분집합 생성
def makeSubset(s):
    # for b in battery[s + 1:]:
    for b in range(s + 1, N - 1):
        size = len(stopBy)
        for i in range(size):
            stopBy.append(stopBy[i] + [[b, battery[b]]])


T = int(input())

for tc in range(1, T + 1):
    N, *battery = map(int, input().split())
    must = []
    i = 0
    # 공집합 대신 무조건 들어가야 하는 충전지 정보를 미리 추가해둠
    # 충전지에서 충전 가능한 양이 1인 경우 계속 추가
    while i < N - 3:
        if i == 0:
            must.append([i, battery[i]])
        if must[-1][1] == 1:
            must.append([i + 1, battery[i + 1]])
        i += 1

    stopBy = [must]
    num = N - 1

    # 1. 부분집합 생성
    makeSubset(must[-1][0])

    # 2. 완전 탐색을 통해 부분집합의 length가 가장 작은 것 선택
    for stop in stopBy:
        bus = 0
        possible = True
        for i in range(1, len(stop)):
            bus += stop[i - 1][1]
            # 선택된 충전지 전까지의 충전 값이 해당 충전지의 인덱스 값 미만인 경우
            # 무조건 안되는 케이스이므로 break
            if bus < stop[i][0]:
                possible = False
                break

        if not possible:
            continue
        
        # 가능한 케이스로 걸러진 것들 중에 가장 길이가 짧은 것을 선택
        if sum([stop[i][1] for i in range(len(stop))]) >= N - 1:
            if len(stop) == 4:
                print(stop)
            if num > len(stop):
                num = len(stop)

        print(f'sum = {sum([stop[i][1] for i in range(len(stop))])}')
        print()


    print(f'#{tc} {num - 1}')