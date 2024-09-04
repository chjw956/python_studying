# 이진 탐색 소스코드 구현(재귀 함수)
def binary_search_recur(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    # 찾은 경우 중간점 인덱스를 반환함
    if array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽을 확인함
    elif array[mid] > target:
        return binary_search_recur(array, target, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽을 확인함
    else:
        return binary_search_recur(array, target, mid + 1, end)


# 이진 탐색 소스코드 구현(반복문)
def binary_search_for(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        # 찾은 경우, 중간점 인덱스를 반환함
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우, 왼쪽을 확인함
        elif array[mid] > target:
            end = mid - 1
        else:
        # 중간점의 값보다 찾고자 하는 값이 큰 경우, 오른쪽을 확인함
            start = mid + 1
    return None


array = [2, 4, 7, 9, 11, 19, 23]
N = len(array)      # N: 원소의 개수
target = 7          # 목표 값

# 이진 탐색 수행 결과 출력
result = binary_search_recur(array, target, 0, N - 1)
# result = binary_search_for(array, target, 0, N - 1)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result)           # 2