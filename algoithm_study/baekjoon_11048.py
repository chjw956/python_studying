# 백준 11048. 이동하기 (silver 2) - DP
# NxM 크기의 미로에서 (1, 1)에서 (N, M)으로 이동하면서 각 방의 사탕을 가져간다고 할 때,
# 준규가 가져올 수 있는 사탕의 최대 개수를 구하라.
# (단, 이동 방향은 오른쪽, 아래쪽, 대각선 오른쪽 아래 방향으로만 가능하다.)

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    miro = [list(map(int, input().split())) for _ in range(N)]

