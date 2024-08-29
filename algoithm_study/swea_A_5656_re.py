# SWEA [A형 대비 1] 5656. 벽돌 깨기
# 구슬을 쏘아 벽돌을 깨트리는 게임이다. 
# 구슬은 N번만 쏠 수 있고, 벽돌들은 W x H 배열로 주어진다.
# 벽돌은 1 ~ 9의 수로 표현되며, 0은 비어있는 지점을 의미한다.
# 구슬이 명중한 벽돌은 상하좌우 (벽돌에 적힌 숫자 - 1)칸 만큼의 벽돌이 같이 제거된다.
# 또한 벽돌 사이에 빈 공간이 생기는 경우, 벽돌은 중력에 의해 밑으로 내려가게 된다.
# N개의 벽돌을 떨어트려 최대한 많은 벽돌을 제거하려 할 때, 남은 벽돌의 개수를 구하라.
# 상웅 팁: 순열로 완전 탐색하여 풀이하라!

# 1열부터 W열까지 구슬을 칠 열을 순열로 생성

import sys
sys.stdin = open('sample_input\sample_input(4).txt', 'r')


# 백트래킹 활용 순열
def backtrack_perm(arr, k, used):
    global permutations

    if len(arr) == k:
        permutations.append(arr)

    for i in range(len(array)):
        if used[i] == False:
            used[i] = True
            backtrack_perm(arr + [array[i]], k, used)
            used[i] = False


T = int(input())

for tc in range(1, T + 1):
    # N: 구슬을 쏘는 횟수, W x H: 주어진 배열의 크기
    N, W, H = map(int, input().split())
    array = list(i for i in range(0, W))
    used = [False for i in range(len(array))]
    permutations = []

    backtrack_perm(array, N, used)