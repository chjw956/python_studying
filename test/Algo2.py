# 문제2 : 외계인 자리 배정
# 외계인들을 줄 세웠을 때의 최소 위험도 출력 프로그램

# 각 행 기준 가장 작은 값을 먼저 잡아서 최소 루트를 만든 후에 그중에 가장 작은 값을 출력하면 될 듯..
# 아 잘못 풀었어ㅠ

import sys
from collections import deque
sys.stdin = open('algo2_sample_in.txt', 'r')


def searchSafe(graph, i, j, n):
    visited = [[[] for i in range(n)] for i in range(n)]

    root = [i, j]

    for num in graph[j]:
        


# 최소 위험도를 찾는 메서드
def searchSafe(arr, n):
    # 위험도 기준 오름차순 정렬
    arr.sort(key=lambda x:x[0])

    # 가장 낮은 위험도 값을 저장해둘 스택 생성
    dangers = []
    least_danger = []

    for i in range(len(arr)):
        # 경로
        root = [arr[i][1][0], arr[i][1][1]]
        danger = arr[i][0]
    
        for a in arr[i + 1:]:
            if a[1][0] == root[-1] and a[1][1] not in root:
                # print(f'{arr[i][1][1]} -> {a[1][1]} danger = {a[0]}')
                danger += a[0]
                root.append(a[1][1])
                print(danger, root)
        
        if len(root) == N:
                print(f'i = {i}, dangers = {dangers}')
                print()
                dangers.append(danger)
        else:
            continue

    print(dangers)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())            # N : 외계인의 수

    # 외계인들의 위험도 맵
    matrix = [list(map(int, input().split())) for _ in range(N)]

    array = []

    for i in range(N):
        for j in range(N):
            # 자기자신까지의 위험도인 0의 값은 제외시킴
            if matrix[i][j] == 0:
                continue
            # 위험도 값과 시작점(i)에서 도착점(j)까지의 정보를 함께 저장
            array.append([matrix[i][j], [i, j]])

    print(f'#{tc}', end = ' ')
    searchSafe(array, N)