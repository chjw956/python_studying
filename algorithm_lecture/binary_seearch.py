# 이진 탐색 소스코드 구현(재귀 함수)
# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2

#     # 찾은 경우 중간점 인덱스를 반환함
#     if array[mid] == target:
#         return mid
#     # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽을 확인함
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid - 1)
#     # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽을 확인함
#     else:
#         return binary_search(array, target, mid + 1, end)
    

# # N(원소의 개수)와 target(찾고자 하는 문자열)을 입력받음
# N, target = list(map(int, input().split()))

# # 전체 원소 입력받기
# array = list(map(int, input().split()))

# # 이진 탐색 수행 결과 출력
# result = binary_search(array, target, 0, N - 1)

# if result == None:
#     print("원소가 존재하지 않습니다.")
# else:
#     print(result + 1)



# 이진 탐색 소스코드 구현(반복문)
def binary_search(array, target, start, end):
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

# N(원소의 개수)과 target(찾고자 하는 문자열)을 입력받음
N, target = list(map(int, input().split()))

# 전체 원소 입력받기
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, N - 1)

if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)