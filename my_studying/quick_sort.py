# <이것이 취업을 위한 코딩 테스트다 - 나동빈> 퀵 정렬

# (전통) 퀵 정렬 소스코드
def quick_sort(array, start, end):
    if start >= end:                # 원소가 1개인 경우 종료
        return 
    
    pivot = start
    big = start + 1
    small = end

    while big <= small:
        # pivot보다 큰 데이터를 찾을 때까지 반복
        while big <= end and array[big] <= array[pivot]:
            big += 1
        
        # pivot보다 작은 데이터를 찾을 때까지 반복
        while small > start and array[small]>= array[pivot]:
            small += 1
        
        # 엇갈렸다면 작은 데이터와 피벗을 교체
        if big > small:
            array[small], array[pivot] = array[pivot], array[small]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else:
            array[small], array[big] = array[big], array[small]
        
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행 -> 여기 인덱스가 이해가 안 됨
    quick_sort(array, start, small - 1)
    quick_sort(array, small + 1, end)


# 파이썬의 장점을 살린 퀵 정렬 소스코드
def quick_sort_py(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0]        # 피벗은 첫 번째 원소
    tail = array[1:]        # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]         # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot]         # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환함
    return quick_sort_py(left_side) + [pivot] + quick_sort_py(right_side)


array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
quick_sort(array, 0, len(array) - 1)
print(array)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
print(quick_sort_py(array))