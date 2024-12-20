# SWEA 5656. 벽돌깨기(D4)
# python 15초, java 3초
# 구슬을 쏘아 벽돌을 깨트리는 게임을 할 때, 구슬은 N번만 쏠 수 있으며 벽돌들의 정보는 W x H의 배열로 입력된다. 
# 배열에서의 0은 빈 공간을 의미하며, 구슬이 명중한 벽돌은 상하좌우로 (벽돌에 적힌 숫자 - 1)칸 만큼의 벽돌까지 깨트린다. 
# 또한 벽돌이 깨지면서 생긴 빈 공간은 중력의 영향으로 아래로 벽돌들이 떨어지며 메워진다고 할 때, 
# N번 구슬을 쏘아 최대한 많은 벽돌을 제거한다면 남은 벽돌의 개수는 얼마인가?

import sys
sys.stdin = open('sample_input\sample_input(4).txt', 'r')
from copy import deepcopy


# 순서 조합을 만들어 반환
def makeOrder(empty, chance, w):
    global chances
    
    if len(empty) == chance:
        chances.append(empty)
        return
    
    for i in range(w):
        makeOrder(empty + [i], chance, w)


# 입력된 지도에 대해 n번째 열의 시작 행을 찾아 반환
def findStart(arr, n, h):
    for i in range(h):
        if arr[i][n]:
            return i
    return -1


# r: 구슬을 쏘는 지점의 행, l: 구슬을 쏘는 지점의 열, power: 처음 호출 시, 0 입력됨
def breakBrick(r, l, power):
    global breaking
    # 현재 지점 정보 기반 power 갱신
    if breaking[r][l] - 1 > power:
        power = breaking[r][l] - 1

    breaking[r][l] = 0

    if power < 1:
        return

    for d in directions:
        mi = r + d[0]
        mj = l + d[1]
        
        # 지도 범위 내에 있다면
        if 0 <= mi < H and 0 <= mj < W:
            breakBrick(mi, mj, power - 1)


def gravity(arr, w, h):
    global chance
    cnt = 0
    for i in range(h-1, -1, -1):
        for j in range(w):
            # 벽돌이 있다면 남은 벽돌 수 카운팅 +1
            if arr[i][j]:
                cnt += 1

            # 벽돌이 없는 빈 공간이라면 위에서 한 칸씩 밑으로 내림
            if (not arr[i][j]) and arr[i - 1][j]:
                if i - 1 >= 0:
                    arr[i][j] = arr[i - 1][j]
                    arr[i - 1][j] = 0
                    cnt += 1
    return cnt


# 상 하 좌 우
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]] 

T = int(input())
T = 1

for tc in range(1, T + 1):
    # N: 구슬을 쏘는 횟수, W x H: 벽돌 배열의 크기
    N, W, H = map(int, input().split())

    bricks = [list(map(int, input().split())) for _ in range(H)]
    min_rest = W * H

    chances = []

    makeOrder([], N, W)

    for chance in chances:
        breaking = deepcopy(bricks)

        for c in chance:
            target = findStart(breaking, c, H)
            if target == -1 :
                continue
            breakBrick(target, c, 0)

            if chance == [2, 2, 6]:
                print(f'c = {c}, target = {target}')
                for b in breaking:
                    print(b)
                print()

            # 벽돌 + 중력 효과
            remain = gravity(breaking, W, H)    

            

        min_rest = min(min_rest, remain)
    
    print(f'#{tc} {min_rest}')
    