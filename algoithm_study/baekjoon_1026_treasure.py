# 백준 1026번 보물 (silver4)
import sys
sys.stdin = open('sample_input\sample_input(1).txt', 'r')


def quick_sort(array, start, end):
        if start >= end:
            return
        
        pivot = start
        big = start + 1
        small = end

        while big <= small:        
            while big <= end and array[big] <= array[pivot]:
                big += 1
            while small > start and array[small] >= array[pivot]:
                small -= 1

            if big > small :
                array[small], array[pivot] = array[pivot], array[small]
            else:
                array[small], array[big] = array[big], array[small]
        
        quick_sort(array, start, small - 1)
        quick_sort(array, small + 1, end)
    

def quick_sort_md(array, start, end):
        if start >= end:
            return
        
        pivot = start
        big = start + 1
        small = end

        while big <= small:        
            while big <= end and array[big][0] <= array[pivot][0]:
                big += 1
            while small > start and array[small][0] >= array[pivot][0]:
                small -= 1

            if big > small :
                array[small], array[pivot] = array[pivot], array[small]
            else:
                array[small], array[big] = array[big], array[small]
        
        quick_sort(array, start, small - 1)
        quick_sort(array, small + 1, end)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    sorted_A = [0] * len(A)
    B_idx = [(B[i], i) for i in range(len(B))]
    total = 0

    quick_sort(A, 0, len(A) - 1)
    quick_sort_md(B_idx, 0, len(B_idx) - 1)

    for i in range(len(A)):
        sorted_A[B_idx[len(A) - i - 1][1]] = A[i]

    # 총합(total) 구하기
    for i in range(len(A)):
        total += sorted_A[i] * B[i]

    print(f'#{tc} {total}')