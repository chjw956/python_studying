# SWEA 24.09.04.(수)- 14229. 백만 개의 정수 정렬
import sys
sys.stdin = open('sample_input\sample_input(54).txt', 'r')

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


# 백만 개의 정수 입력
A = list(map(int, input().split()))
quickSort(A, 0, len(A) - 1)

print(A[500000])