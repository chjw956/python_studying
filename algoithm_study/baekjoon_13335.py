# 백준 13335. 트럭(silver 1)
# 강 위의 다리를 n개의 트럭이 건너려고 한다.
# e다리 위에는 w대의 트럭만이 동시에 올라갈 수 있다고 할 때, 
# 모든 트럭들이 다리를 건너는 최단 시간을 출력하라.
# 단, 트럭의 순서는 변경할 수 없으며 트럭의 무게는 서로 같지 않을 수 있다.
# 참고로, 트럭들은 하나의 단위 시간에 하나의 단위 길이만큼만 이동할 수 있다고 가정한다.
# 시간 제한 1초

import sys
sys.stdin = open('sample_input\sample_input(23).txt.', 'r')


def whosNext(k):
    global group, n, L
    for i in range(k, n + 1):
        if group + weights[i] <= L:
            group += weights[i]
        else:
            return i
    return k


T = int(input())

for tc in range(1, T + 1):
    # n: 트럭의 수, w: 다리 길이, L: 다리의 최대 하중
    n, w, L = map(int, input().split())
    weights = [0]
    weights += [i for i in map(int, input().split())]

    startTruck = 1
    group =  weights[startTruck]
    nextTruck = whosNext(startTruck + 1)
    needTime =  w - 1            # 첫 번째 트럭이 도착하기 직전 상황에서 반복문 시작

    while startTruck != n :
        if nextTruck <= n:
            if group + weights[nextTruck] <= L:
                group += weights[nextTruck]
                nextTruck += 1
                needTime += 1
            else:
                needTime += 1
                group -= weights[startTruck]
                startTruck += 1
        else:
            needTime += 1
            group -= weights[startTruck]
            startTruck += 1

    print(needTime)            