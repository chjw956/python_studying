# 백준 13335. 트럭(silver 1)
# 강 위의 다리를 n개의 트럭이 건너려고 한다.
# 다리 위에는 w대의 트럭만이 동시에 올라갈 수 있다고 할 때, 
# 모든 트럭들이 다리를 건너는 최단 시간을 출력하라.
# 단, 트럭의 순서는 변경할 수 없으며 트럭의 무게는 서로 같지 않을 수 있다.
# 참고로, 트럭들은 하나의 단위 시간에 하나의 단위 길이만큼만 이동할 수 있다고 가정한다.
# 시간 제한 1초

import sys
from tracemalloc import start
sys.stdin = open('sample_input\sample_input(23).txt.', 'r')

from collections import deque

T = int(input())

for tc in range(1, T + 1):
    """
    # 내가 푼 코드 (틀림)
    # n: 트럭의 수, w: 다리 길이, L: 다리의 최대 하중
    n, w, L = map(int, input().split())
    weights = [0]
    weights += [i for i in map(int, input().split())]

    startTruck = 1
    nextTruck = 2
    group =  weights[startTruck]
    needTime =  1 

    while nextTruck <= n:
        if group + weights[nextTruck] <= L and nextTruck - startTruck <= w:
            group += weights[nextTruck]
            nextTruck += 1
            needTime += 1
        else:
            needTime += w - (nextTruck - startTruck) + 1
            group -= weights[startTruck]
            startTruck += 1
            if group + weights[nextTruck] <= L:
                group += weights[nextTruck]
                nextTruck += 1

    if needTime < w:
        needTime += w - (nextTruck - startTruck)

    print(needTime + (n - startTruck + 1))
    """

    """
    # 구글링한 답안
    # n: 트럭의 수, w: 다리 길이, L: 다리의 최대 하중
    n, w, L = map(int, input().split())
    cars = list(map(int, input().split()))

    # 큐를 이용해서 구현
    # 처음에 다리의 길이만큼 0을 넣어준다 -> 차가 다리에 들어와서 나가는 거 시간 카운트할 수 있도록 빈 공간을 넣어준다.
    q = deque()
    for _ in range(w):
        q.append(0)

    time = 0
    idx = 0

    while idx < n:
        time += 1
        q.popleft()

        # 지금 차 들어가도 다리 하중이 넘지 않는 경우
        if sum(q) + cars[idx] <= L:
            q.append(cars[idx])
            idx += 1
        # 넘으면 이전 차만 앞으로 가는 거고 빈공간이 생기는 거니까 0 넣어줌
        else:
            q.append(0)

    # 다리에 차가 다 나가야 하므로 큐가 빌때까지
    while q:
        time += 1
        q.popleft()

    print(time)
    """
    

    # 다시 풀어봄
    # n: 트럭의 수, w: 다리 길이, L: 다리의 최대 하중
    n, w, L = map(int, input().split())
    weights = list(map(int, input().split()))
    through = []

    q = deque()

    q.append(weights[0])
    weight_sum = weights[0]
    i = 1

    while i < n:
        # 다리 위가 꽉 찼을 때
        if len(q) >= w:
            through.append(q.popleft())
            weight_sum -= through[-1]
            continue
        if weight_sum + weights[i] <= L:
            q.append(weights[i])
            weight_sum += weights[i]
            i += 1
        else:
            q.append(0)  

    for _ in range(len(q)):
        through.append(q.popleft())

    for _ in range(w):
        through.append(0)
    print(len(through))