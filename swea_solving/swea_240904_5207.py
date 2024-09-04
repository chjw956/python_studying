# SWEA 24.09.04.(수) - 5207. [파이썬 S/W 문제해결 구현] 4일차 - 이진 탐색 (D3)
# A 리스트와 B 리스트가 주어질 때, B에 저장된 M개의 정수에 대해 A에 들어있는 수인지 이진 탐색으로 확인하고자 한다.
# B에 속한 어떤 수가 A에 들어있으면서 동시에 탐색 과정에서 양쪽 구간을 번갈아 선택하게 되는 숫자의 개수를 출력하라.

import sys
sys.stdin = open('sample_input\sample_input(55).txt', 'r')


# 이진 탐색 소스코드 구현(반복문)
def binary_search_for(array, target, start, end):
    global side

    while start <= end:
        mid = (start + end) // 2

        # 찾은 경우, 중간점 인덱스를 반환함
        if array[mid] == target:
            side = 0
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우, 왼쪽을 확인함
        elif array[mid] > target:
            if side == -1:
                return None
            side = -1
            end = mid - 1
        else:
        # 중간점의 값보다 찾고자 하는 값이 큰 경우, 오른쪽을 확인함
            if side == 1:
                return None
            side = 1
            start = mid + 1
    return None



T = int(input())

for tc in range(1, T + 1):
    # N: A 리스트 길이, M: B 리스트 길이
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A.sort()

    cnt = 0

    for b in B:
        # 왼쪽은 -1, 중간은 0, 오른쪽은 1이라고 하자.
        side = 0
        # A에 값이 존재할 때
        if binary_search_for(A, b, 0, N - 1) != None:
            # 번갈아 탐색한 경우
            if side == 0:
                cnt += 1
    print(f'#{tc} {cnt}')