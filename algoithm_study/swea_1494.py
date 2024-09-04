# SWEA 1494.사랑의 카운슬러 (D4)
# 지렁이가 N마리 있을 때, 지렁이 2마리를 매칭시키고자 한다.
# 모든 지렁이들을 매칭시키되, 지렁이들이 움직인 벡터의 크기 합이 최소가 되도록 하라.
# 문제는 어렵지 않은데 시간 초과;

import sys
sys.stdin = open('sample_input\sample_input(9).txt', 'r')

# 두 점 사이의 벡터 크기 계산
def calDist(x1, y1, x2, y2):
    return x1 - x2, y1 - y2


# 순열
def permutation(empty, lst, k, used):
    global worm_perm

    if len(empty) == k:
        worm_perm.append(empty)
        return
    
    for l in lst:
        if not used[l[0]]:
            used[l[0]] = True
            permutation(empty + [l[0]], lst, k, used)
            used[l[0]] = False


T = int(input())

for tc in range(1, T + 1):
    # N: 지렁이 마리 수
    N = int(input())
    worms = [list(map(int, input().split())) for _ in range(N)]
    worm_perm = []

    # 입력된 순서로 지렁이 번호 붙여줌
    for i in range(1, N + 1):
        worms[i - 1] = (i, worms[i - 1])

    used = [False] * (N + 1)
    permutation([], worms, N, used)

    short_cut = 1000000 ** 2

    for p in worm_perm:
        x = y = 0
        for i in range(0, N - 1, 2):
            x1 = worms[p[i] - 1][1][0]
            y1 = worms[p[i] - 1][1][1]

            x2 = worms[p[i + 1] - 1][1][0]
            y2 = worms[p[i + 1] - 1][1][1]

            dx, dy = calDist(x1, y1, x2, y2)
            x += dx
            y += dy

        short_cut = min(short_cut, x ** 2 + y ** 2)

    print(f'#{tc} {short_cut}')