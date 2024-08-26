# SWEA [A형 대비 1] 5656. 벽돌 깨기
# 구슬을 쏘아 벽돌을 깨트리는 게임이다. 
# 구슬은 N번만 쏠 수 있고, 벽돌들은 W x H 배열로 주어진다.
# 벽돌은 1 ~ 9의 수로 표현되며, 0은 비어있는 지점을 의미한다.
# 구슬이 명중한 벽돌은 상하좌우 (벽돌에 적힌 숫자 - 1)칸 만큼의 벽돌이 같이 제거된다.
# 또한 벽돌 사이에 빈 공간이 생기는 경우, 벽돌은 중력에 의해 밑으로 내려가게 된다.
# N개의 벽돌을 떨어트려 최대한 많은 벽돌을 제거하려 할 때, 남은 벽돌의 개수를 구하라.

# import sys
# sys.stdin = open('sample_input\sample_input(4).txt', 'r')\

# 2차원 배열 반시계 방향 90도 회전 함수
def spin(arr, w, h):
    spun = []
    
    for j in range(w-1 , -1, -1):
        line = []
        for i in range(h):
            line.append(arr[i][j])
        spun.append(line)

    return spun


# 배열에서 가장 큰 수의 인덱스를 반환하는 함수
def biggest(arr, l):
    big = 0 
    idx = -1
    for i in range(l):
        if big < arr[i]:
            big = arr[i]
            idx = i
    
    return idx


def hitBrick(arr, i, j, w, h):
    power = arr[i][j] - 1
    print(f'power = {power}')
    print(f'i = {i}, j = {j}')

    # 구슬 맞은 부위를 0으로 변경함
    arr[i][j] = 0

    if power == 0:
        return arr

    # for문을 하나로 합쳐야 재귀에서 power 값이 동시에 적절하게 적용될 듯!
    toGo = []

    # 십자 모양 만들기!
    for k in range(i - power, i + power + 1):
        for l in range(j - power, j + power + 1):
            if k == i and [k, l] not in toGo:
                toGo.append([k, l])
            if l == j and [k, l] not in toGo:
                toGo.append([k, l])

    print(f'toGo = {toGo}')

    for k in range(j - power, j + power + 1):
        for l in range(i - power, i + power + 1):
            

            if 0 <= k < h:
                if arr[i][k] - 1 > power:
                    hitBrick(arr, i, k, w, h)
                else:
                    arr[i][k] = 0
    
    for k in range(i - power, i + power + 1):
        if 0 <= k < w:
            if arr[k][j] - 1 > power:
                hitBrick(arr, i, k, w, h)
            else:
                arr[k][j] = 0


# T = int(input())
T = 1

for tc in range(1, T + 1):
    N, W, H = map(int, input().split())

    wall = [list(map(int, input().split())) for _ in range(H)]

    # 입력된 벽돌 배열을 반시계 방향으로 90도 회전시킴
    wall = spin(wall, H, W)

    # 구슬을 N번 칠 수 있음
    for n in range(N):
        sum_values = []

        for w in range(W):
            sum_value = 0
            for h in range(H):
                sum_value += wall[w][h]
            sum_values.append(sum_value)
        
        # 벽돌 숫자의 합이 가장 큰 행의 인덱스 반환
        idx = biggest(sum_values, H)

        for h in range(H):
            if wall[idx][h] != 0:
                start = h
                break
        print(f'idx = {idx}, start = {start}')
        
        # 구슬을 치고난 효과를 구현
        wall = hitBrick(wall, idx, start, W, H)

        print(wall)
        print()
