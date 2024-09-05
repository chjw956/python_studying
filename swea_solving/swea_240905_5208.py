# SWEA 24.09.05.(목) - 5208. [파이썬 S/W 문제해결 구현] 5일차-전기버스2 (D3)
# 전기 버스의 충전지가 방전되기 전에 정류장에서 교체하여 계속 운행해야 한다.
# 이때, 목적지에 도달하기 위한 최소한의 교체 횟수를 출력하라.
# 참고로 마지막 정류장엔 배터리가 없으며, 출발지에서의 배터리 장착은 교체 횟수에 포함하지 않는다.
# 수정해야 함

import sys
sys.stdin = open('sample_input\sample_input(58).txt', 'r')


# 비트맵에 따라 부분 집합을 만들어주는 작업 수행
def makeSubset(arr, bit_arr):
    subset = []
    for i in range(len(bit_arr)):
        if bit_arr[i] == 1:
            subset.append(arr[i])
    return subset


# 부분 집합
def powerset(arr, bit_arr, idx):
    global subsets

    # 첫 번째 버스정류장 제외 나머지 정류장 대상
    if idx == len(arr):
        subsets.append(makeSubset(arr, bit_arr))
        return
    
    # 0 또는 1 입력
    for i in range(2):
        bit_arr[idx] = i
        powerset(arr, bit_arr, idx + 1)


T = int(input())
T = 2

for tc in range(1, T + 1):
    bus_stops = list(enumerate(list(map(int, input().split()))))
    N = bus_stops[0][1]             # 정류장 개수    
    min_stopby = N - 2              # 모든 정류장을 들리는 횟수로 초기화
    subsets = []                    # 출발지 제외 나머지 정류장들에 대한 부분집합
    cases = []                      # 가능한 케이스
    
    powerset(bus_stops[2:], [None] * (N - 2), 0)

    # 부분집합들에 대해 순회하며 가능한 것 체크 + 최소 횟수 초기화(update)
    for s in subsets:
        bus = bus_stops[1][1]           # 버스가 출발지에서 충전되는 파워 
        canDrive = True
        if s == []:                     # 공집합은 넘어감
            continue
        s.sort(key=lambda x:x[0])
        stopBy = 0
        for i in range(len(s)):
            bus -= (s[i][0] - 1)     # 이동한 칸 수만큼 파워(-)
            # 버스가 방전됐다면 운행 불가능 케이스로 판단
            if bus < 0  or (s[i][0] != N - 1 and bus == 0):
                canDrive = False
                break
            bus += s[i][1]          # 이동한 곳에서 충전(+)
            stopBy += 1             # 들린 횟수 + 1

        if canDrive:
            cases.append(s)
            min_stopby = min(min_stopby, stopBy)
        
    print(f'#{tc} {min_stopby} {cases}')