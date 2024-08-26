# 문제1: 미생물 이동
# 첫 번째 구역에는 항상 먹이가 있음
# 최대로 몇 번째 구역에 이동할 수 있는지를 출력

import sys
sys.stdin = open('algo1_sample_in.txt', 'r')


def letsGo(arr, N, K):
    # 캐릭터의 현재 위치
    i = 2

    # 캐릭터가 현재 이동할 수 있는 칸의 수
    power = K

    for a in arr:
        if a == 1:
            power += K
        else:
            power -= 1
        
        if i == N or power == 0:
            return i
        i += 1
    return -1



T = int(input())

for tc in range(1, T + 1):
    # N: 활동 구역의 수, K: 먹이를 먹고 이동하는 최대 칸 수
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    rslt = letsGo(arr[1:], N, K)

    print(f'#{tc} {rslt}')
