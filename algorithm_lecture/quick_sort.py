# 퀵 정렬(Quick-sort)

# 1-1. 분할 과정 (호어 분할, Hoare-Partition 알고리즘)
def partition_Hoare(arr, start, end):
    pivot = start
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복함
        while left <= end and arr[left] <= arr[pivot]:
            left += 1

        # 피벗보다 작은 데이터를 찾을 때까지 반복함
        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        # 엇갈렸다면 작은 데이터와 피벗을 교체함
        if left > right: 
            arr[right], arr[pivot] = arr[pivot], arr[right]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체함
        else:
            arr[left], arr[right] = arr[right], arr[left]

    return right


# 1-2. 분할 과정 (로무토 분할, Lomuto Partition 알고리즘)
def partition_Lomuto(arr, start, end):
    pivot = end
    left = start - 1
    
    for right in range(start, pivot):
        if arr[right] <= arr[pivot]:
            left += 1
            arr[left], arr[right] = arr[right], arr[left]
                
    arr[left + 1], arr[pivot] = arr[pivot], arr[left + 1]

    return left + 1            # 최종적으로 pivot이 위치하는 인덱스를 반환함


# 2. 정렬 과정
def quick_sort(arr, start, end):
    # 원소가 1개인 경우 종료
    if start >= end:
        return
    
    # right = partition_Hoare(arr, start, end)
    right = partition_Lomuto(arr, start, end)

    quick_sort(arr, start, right - 1)
    quick_sort(arr, right + 1, end)

arr = [3, 1, 4, 6, 9, 2, 8, 7, 5]

quick_sort(arr, 0, len(arr) - 1)
print(arr)              # [1, 2, 3, 4, 5, 6, 7, 8, 9]