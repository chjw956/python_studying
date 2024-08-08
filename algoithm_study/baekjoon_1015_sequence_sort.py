# 백준 1015번 수열 정렬 (silver4)

# 배열 A가 주어졌을 때, 수열 P를 적용한 결과가 비내림차순이 되는 수열을 찾는 프로그램
# 비내림차순 : 각각의 원소가 바로 앞에 있는 원소보다 크거나 같을 경우
#             만약 그러한 수열이 여러개라면 사전순으로 앞서는 것을 출력함

import sys
sys.stdin = open('sample_input\sample_input(3).txt', 'r')


# 퀵 정렬
def quick_sort(arr, start, end):
    if start >= end:
        return
    
    pivot = start
    big = start + 1
    small = end

    while small >= big:
        while big <= end and arr[big] <= arr[pivot]:
            big += 1
        while small > start and arr[small] >= arr[pivot]:
            small -= 1

        if big > small:
            arr[small], arr[pivot] = arr[pivot], arr[small]
        else:
            arr[small], arr[big] = arr[big], arr[small]
    
    quick_sort(arr, start, small - 1)
    quick_sort(arr, small + 1, end)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    sorted_A = A[:]
    B = [0] * len(A)
    P = [i for i in range(N)]

    quick_sort(sorted_A, 0, len(A) - 1)
    
    for (i, s) in enumerate(sorted_A):
        sorted_A[i] = (i, s)

    for a in A:
        for i in range(len(sorted_A)):
            if sorted_A[i][1] == a :
                print(sorted_A[i][0], end = ' ')
                sorted_A[i] = (0, 0)
                break

    print()
    
    

