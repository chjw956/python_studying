# 백준 4485. 녹색 옷 입은 애가 젤다지? (gold 4)
# NxN 크기의 동굴의 [0, 0]에서 주인공 링크가 동굴의 [N-1, N-1]까지 이동하려고 한다.
# 동굴은 각 칸마다 도둑루피가 있는데, 이 칸을 지나면 해당 도둑루피의 크기만큼 소지한 루피를 잃게 된다.
# 잃는 금액을 최소로 하여 동굴을 건너려고 할 때, 링크가 잃을 수밖에 없는 최소 금액은 얼마인가?
# (단, 링크는 상하좌우 인접한 곳으로 1칸씩 이동할 수 있다.)

import sys
sys.stdin = open('sample_input\sample_input(25).txt', 'r')


# si, sj: 시작 노드 정보
def backtracking_dfs(path, si=0, sj=0):
    global N

    # 처음에 시작점[0, 0] 추가
    if not path:
        path += [(0, 0)]

    if si == N - 1 and sj == N - 1:
        roots.append(list(path))    # 깊은 복사
        return

    for [di, dj] in directions:
        ni = si + di
        nj = sj + dj             
        if 0 <= ni < N and 0 <= nj < N:
            path.append((ni, nj))
            backtracking_dfs(path, ni, nj)
            path.pop()          # 백트래킹으로 경로 상태 복원

    return


T = int(input())

# 아래쪽, 오른쪽 방향
directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

for tc in range(1, T + 1):
    N = int(input())
    cave = [list(map(int, input().split())) for _ in range(N)]
    roots = []

    # 1. 가능한 루트 리스트 모두 생성
    backtracking_dfs([])

    # 2. 생성된 루트들 중에서 최소 합을 갖는 루트를 찾음
    min_minus = 9 * 125 * 125     # 입력 범위의 최대값으로 초기화

    for root in roots:
        minus_rupee = 0
        for ri, rj in root:
            minus_rupee += cave[ri][rj]
            # 2-1. 합해가는 도중에 이미 최소 합보다 큰 값이 돼버렸다면 break
            if minus_rupee > min_minus:
                break
        min_minus = min(min_minus, minus_rupee)
    
    print(f'Problem {tc}: {min_minus}')
