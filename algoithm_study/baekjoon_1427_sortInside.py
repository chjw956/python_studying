# 백준 1427번 소트인사이드 (silver5)

import sys
sys.stdin = open('sample_input\sample_input(2).txt', 'r')

# 내림차순 퀵 정렬 함수
def quick_sort_to_small(array, start, end):
    if start >= end:
        return
    
    pivot = start
    small = start + 1
    big = end

    while small <= big:
        while small <= end and array[small] >= array[pivot]:
            small += 1
        while big > start and array[big] <= array[pivot]:
            big -= 1
        
        if small > big:
            array[big], array[pivot] = array[pivot], array[big]
        else:
            array[small], array[big] = array[big], array[small]
    
    quick_sort_to_small(array, start, big - 1)
    quick_sort_to_small(array, big + 1, end)


T = int(input())

for tc in range(1, T + 1):
    inp_lst = list(map(int, input()))

    quick_sort_to_small(inp_lst, 0, len(inp_lst) - 1)
    print(''.join(map(str, inp_lst)))
