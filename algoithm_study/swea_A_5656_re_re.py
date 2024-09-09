# SWEA 5656. 벽돌깨기(D4)
# python 15초, java 3초
# 구슬을 쏘아 벽돌을 깨트리는 게임을 할 때, 구슬은 N번만 쏠 수 있으며 벽돌들의 정보는 W x H의 배열로 입력된다. 
# 배열에서의 0은 빈 공간을 의미하며, 구슬이 명중한 벽돌은 상하좌우로 (벽돌에 적힌 숫자 - 1)칸 만큼의 벽돌까지 깨트린다. 
# 또한 벽돌이 깨지면서 생긴 빈 공간은 중력의 영향으로 아래로 벽돌들이 떨어지며 메워진다고 할 때, 
# N번 구슬을 쏘아 최대한 많은 벽돌을 제거한다면 남은 벽돌의 개수는 얼마인가?

import sys
sys.stdin = open('sample_input\sample_input(4).txt', 'r')
from copy import deepcopy
from collections import deque


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
# BFS 사용
def breakBrick(r, l, power):
    global breaking
    queue = deque([[r, l]])
    
    while queue:
        [r, c] = queue.popleft()

        if breaking[r][c] < 2:
            breaking[r][c] = 0
            continue
        
        # 벽돌에 적힌 수가 2 이상이면
        power = breaking[r][c]
        breaking[r][c] = 0

        for n in range(1, power):
            for d in directions:
                mi = r + d[0] * n
                mj = c + d[1] * n
                
                # 지도 범위 내에 있다면
                if 0 <= mi < H and 0 <= mj < W:
                    queue.append([mi, mj])
                    

def gravity(w, h):
    global breaking
    cnt = 0
    for j in range(w):
        empty = 0
        for i in range(h - 1, -1, -1):
            # 벽돌이 있다면 남은 벽돌 수에 카운트 + 1
            if breaking[i][j]:
                cnt += 1
                if empty and i + empty < h:
                    breaking[i + empty][j] = breaking[i][j]
                    breaking[i][j] = 0
            # 빈 공간이라면
            elif not breaking[i][j]:
                empty += 1
    return cnt


# 상 하 좌 우
directions = [[-1, 0], [1, 0], [0, -1], [0, 1]] 

T = int(input())

for tc in range(1, T + 1):
    # N: 구슬을 쏘는 횟수, W x H: 벽돌 배열의 크기
    N, W, H = map(int, input().split())

    bricks = [list(map(int, input().split())) for _ in range(H)]
    min_rest = W * H

    chances = []

    makeOrder([], N, W)

    for chance in chances:
        remain = 0
        breaking = deepcopy(bricks)

        for c in chance:
            target = findStart(breaking, c, H)
            if target == -1 :
                continue
            breakBrick(target, c, 0)

            # 벽돌 깨기 + 중력 효과
            remain = gravity(W, H)    

        min_rest = min(min_rest, remain)
    
    print(f'#{tc} {min_rest}')