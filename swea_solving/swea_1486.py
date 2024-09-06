# SWEA 24.09.06.(금) - 1486. 장훈이의 높은 선반 (D4)
# 장훈이가 운영하는 서점에는 높이가 B인 선반이 있다.  
# 서점에 N명의 직원이 일하고 있을 때, 선반에 물건을 올리기 위해 직원들이 탑을 쌓아 올라가려 한다.
# 각 점원의 키가 배열로 주어질 때, 높이가 B 이상인 탑 중에서 가장 높이가 낮은 탑의 높이를 출력하라.

import sys
sys.stdin = open('sample_input\sample_input(60).txt', 'r')


# 조합
def combination(empty, target):
    global min_diff
    
    if sum(empty) >= target:
        min_diff = min(min_diff, sum(empty) - target)
        return
    
    for i in range(N):
        if not used[i]:
            used[i] = True
            combination(empty+[heights[i]], target)
            used[i] = False


def recur(sum_h, cnt):
    global min_diff
    # 기저조건 가지치기1
    # 탑의 높이가 선반의 높이와 같거나 높아졌는가
    if sum_h >= B:
        min_diff = min(min_diff, sum_h - B)
        return
    
    # 기저조건 가지치기2
    # 모든 직원에 대해 검사했는가
    if cnt == N:
        return
    
    # 현재 직원 포함시킴
    recur(sum_h + heights[cnt], cnt + 1)
    # 현재 직원 포함 안 시킴
    recur(sum_h, cnt + 1)
    

T = int(input())

for tc in range(1, T + 1):
    # N: 직원 수, B: 선반 높이
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))       # 직원들의 키

    min_diff = 10000 * 20
    used = [False] * N

    recur(0, 0)

    print(f'#{tc} {min_diff}')