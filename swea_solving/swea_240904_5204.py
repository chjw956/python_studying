# SWEA 24.09.04.(수) - 5204. [파이썬 S/W 문제해결 구현] 4일차 - 병합 정렬 (D3)
# 병합 정렬을 이용해 오름차순으로 정렬할 때, 병합 과정에서 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력하라.

import sys
sys.stdin = open('sample_input\sample_input(57).txt', 'r')


# 병합 정렬 - 분할
def merge_sort(arr):
    global cnt

    if len(arr) <= 1:
        return arr

    middle = len(arr) // 2

    left = arr[:middle]
    right = arr[middle:]

    left = merge_sort(left)
    right = merge_sort(right)
    
    if left[-1] > right[-1]:
        cnt += 1

    return merge(left, right)


# 병합 정렬 - 병합
def merge(left, right):
    result = []

    l = r = 0

    while l < len(left) or r < len(right):
        if l < len(left) and r < len(right): 
            if left[l] <= right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1

        elif l < len(left):
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1

    return result


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    arr = merge_sort(arr)

    print(f'#{tc} {arr[N//2]} {cnt}')