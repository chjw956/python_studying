# SWEA 2115. [모의 S/W 역량 테스트] 벌꿀채취 (D2)
# NxN의 벌통에 대해 각 벌통에 있는 꿀의 양이 주어질 때, 최대한 많은 수익을 내고자 한다.
# 두 명의 일꾼이 가로로 연속되는 M개의 벌통을 선택할 수 있다. 단, 두 명의 일꾼이 선택한 벌통은 겹치면 안된다.
# 두 일꾼이 각자 채취할 수 있는 꿀의 최대 양이 C일 때, 수익의 합이 최대가 되는 경우를 찾고 최대 수익을 출력하라.
# 수익은 각 벌통의 꿀의 양을 제곱하여 합한 값이 된다.

import sys

sys.stdin = open('..\sample_input\sample_input(12)_1.txt', 'r')


# def comb(arr, empty, sum_h, start):
#     global C
#     if start == N or (start < N - 1 and sum_h + honey_bsck[arr[start + 1][0]][arr[start + 1][1]] > C):
#         select.append(empty)
#         return
#
#     for i in range(start, len(arr)):
#         print(f'arr = {arr}, sum_h = {sum_h}')
#         if sum_h + honey_bsck[arr[i][0]][arr[i][1]] <= C:
#             empty.append(arr[i])
#             print(f'empty = {empty}', end=' ')
#             sum_h += honey_bsck[arr[i][0]][arr[i][1]]
#             print(f'sum_h = {sum_h}')
#             comb(arr, empty, sum_h, i + 1)  # 재귀 호출
#             # empty.pop()


def comb(aAndB, empty, start):
    if len(empty) == 2:
        ab.append(aAndB)
        return

    for i in range(start, len(collection)):
        if aAndB:
            if aAndB[-1][0][0] != collection[i][0][0] \
                or
        aAndB.append(collection[i])
        comb(aAndB, empty+[collection[i]], i + 1)
        aAndB.pop()


def makeSubset(arr):
    subsets = [[]]
    for a in arr:
        size = len(subsets)
        for s in range(size):
            subsets.append(subsets[s] + [a])
    return subsets


T = int(input())

for tc in range(1, T + 1):
    # N: 벌통 크기, M: 선택 가능한 벌통 개수, C: 각 일꾼이 채취할 수 있는 최대 꿀의 양
    N, M, C = map(int, input().split())
    honey_bsck = [list(map(int, input().split())) for _ in range(N)]

    collection = []
    honey_amt = []
    total_honey = 0

    # 1. 각 행에서 선택 가능한 벌통 M개 리스트 생성
    for i in range(N):
        for j in range(N - M + 1):
            c = []
            for m in range(M):
                c.append([i, j + m])
            collection.append(c)

    print(f'collection = {collection}')

    # 2. 생성한 collection에서 2개(a, b)를 선택 (겹치지 않는다는 조건을 만족)
    ab = []
    for i in range(len(collection)):
        comb([], [], i)










    # 1-2. 만들어진 조합에 대해 두 일꾼이 선택 가능한 부분집합을 모두 생성함
    selected = []
    for i in range(len(collection)):
        select = makeSubset(collection[i])
        print(f'select = {select}')
        for k in range(1, len(select)):
            a_sum = b_sum = 0
            a_honey = select[k]
            for s in range(k + 1, len(select)):
                b_honey = select[k]
                if a_honey[-1][]
                for a in a_honey:
                    a_sum += honey_bsck[a[0]][a[1]]
                for b in b_honey:
                    b_sum += honey_bsck[b[0]][b[1]]

                if a_sum <= C and b_sum <= C:
                    selected.append([a_honey, b_honey])

    print(f'최종 selected = {selected}')

    # 1-2. 만들어진 조합에서 한 명의 일꾼이 획득 가능한 최대 꿀의 양을 조사함

    # 2. 만들어진 조합 set에서 겹치지 않는 조합 set 2개를 선택함

    # for i in range(len(collection)):
    #     for j in range(i + 1, len(collection)):
    #         select = [collection[i]]
    #         if collection[j][0][0] != collection[i][-1][0] or collection[j][0][1] > collection[i][-1][1]:
    #             select.append(collection[j])
    #             selected.append(select)

    # for s in selected:
    #     print(f'select = {s}')

    # # 3. 선택된 조합 set 2개 중에서 수익이 최대가 되는 것 선택

    # for i in range(0, len(selected)):
    #     sum_v = 0
    #     for j in range(len(selected[i])):
    #         for k in range(len(selected[i][j])):
    #             sum_v += honey_bsck[selected[i][j][k][0]][selected[i][j][k][1]] ** 2
    #     print(f'sum_v = {sum_v}')
    #     total_honey = max(sum_v, total_honey)

    print(f'#{tc} {total_honey}')