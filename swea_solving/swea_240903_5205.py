# SWEA 24.09.03.(수) - 5205. [파이썬 S/W 문제해결 구현] 4일차 - 퀵 정렬 (D3)
# 퀵 정렬을 구현해 N개의 정수를 리스트 A에 정렬해 넣고, A[N//2]를 출력하라.
import sys
sys.stdin = open('sample_input\sample_input(56).txt', 'r')


# 퀵 정렬
def quickSort(arr, start, end):
    if start >= end:
        return
    
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left > right:
            arr[pivot], arr[right] = arr[right], arr[pivot]
        else:
            arr[left], arr[right] = arr[right], arr[left]

    quickSort(arr, start, right - 1)
    quickSort(arr, right + 1, end)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))

    quickSort(A, 0, N - 1)

    print(f'#{tc} {A[N//2]}')