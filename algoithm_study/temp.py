"""
# 시간 초과난 코드(1)

def binary_search(array, target, start, end, difference):
    # 타겟 값과 가장 차이가 적은 값을 찾는 것이 목적!
    if start > end:
        return difference
    
    mid = (start + end) // 2

    # 종료(반환) 조건
    if target - array[mid] < difference:
        return binary_search(array, target, start, mid - 1, target - array[mid])
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽을 확인함
    elif target - array[mid] == 0:
        v = array[mid]
        while array.count(v) != 0:
            # 제거하니까 반환되는 인덱스 값이 기존의 리스트와 달라서 값을 끌어올 수 없음
            array.remove(v)
        return binary_search(array, target, 0, len(array) - 1, 0)
    else :
        return binary_search(array, target, mid + 1, len(array) - 1, target - array[mid])


if __name__ == '__main__':
    N = int(input())        # 수열의 크기 N
    A = list(map(int, input().split()))

    A.sort()
    arr = A[:]
    
    result = [arr[(len(arr)-1)//2]]
    idx = -1

    while len(arr) > 0 : 
        criterion = arr[(len(arr)-1)//2]            # 정렬된 배열 A의 중간값을 기준으로 삼음
        
        # criterion(기준)값보다 작은 값 중에 가장 작은 값을 순차적으로 인덱스로 출력
        difference = binary_search(arr, criterion, idx, len(arr)-1, 0)
        
        value = criterion - difference

        if value in result:
            continue
        else:
            result.append(value)

        idx = A.index(value)
        A.pop(idx)

        arr = A[:]
        
    # result.sort()
    print(len(result))
"""


"""
# 시간 초과난 코드(2)

def binary_search(array, target, start, end, difference):
    # 타겟 값과 가장 차이가 적은 값을 찾는 것이 목적!
    if start > end:
        return difference
    
    mid = (start + end) // 2

    # 종료(반환) 조건
    if target - array[mid] < difference:
        return binary_search(array, target, start, mid - 1, target - array[mid])
    else :
        return binary_search(array, target, mid + 1, len(array) - 1, target - array[mid])


N = int(input())        # 수열의 크기 N
A = list(map(int, input().split()))

A.sort()

mid = A[(len(A)-1)//2]

result = [mid]

cnt = A.count(mid)

for _ in range(cnt):
    A.remove(mid)

while len(A) > 0 : 
    criterion = A[(len(A)-1)//2]            # 정렬된 배열 A의 중간값을 기준으로 삼음
    
    # criterion(기준)값보다 작은 값 중에 가장 작은 값을 순차적으로 인덱스로 출력
    difference = binary_search(A, criterion, 0, len(A)-1, 0)
    
    value = criterion - difference

    if value in result:
        A.remove(value)
        continue
    else:
        result.append(value)

    idx = A.index(value)
    A.pop(idx)
    
print(len(result))
"""


"""
# 시간 초과난 코드(3)


def binary_search(array, target, start, end, difference, idx):
    # 종료(반환) 조건
    if start > end:
        return idx
    
    mid = (start + end) // 2

    if target - array[mid] < difference:
        return binary_search(array, target, start, mid - 1, target - array[mid], mid)
    else :
        return binary_search(array, target, mid + 1, len(array) - 1, target - array[mid], mid)


N = int(input())        # 수열의 크기 N
A = list(map(int, input().split()))

A.sort()

mid = A[(len(A) - 1) // 2]
result = [mid]

cnt = A.count(mid)

for _ in range(cnt):
    A.remove(mid)

cnt = len(A)

for _ in range(cnt):
    length = len(A)
    if length == 0:
        break

    criterion = A[(length - 1) // 2]            # 정렬된 배열 A의 중간값을 기준으로 삼음 
    
    i = binary_search(A, criterion, 0, length - 1, 0, (length - 1) // 2)

    if A[i] in result:
        A.pop(i)
        continue
    else:    
        result.append(A[i])
        A.pop(i)
    
print(len(result))
"""


"""
# 시간 초과난 코드(4)

def binary_search2(array, target, start, end, difference, idx):
    while start <= end:
        mid = (start + end) // 2
        
        if target - array[mid] < difference:
            end = mid - 1
        else:
            start = mid + 1
        idx = mid
    return idx

N = int(input())        # 수열의 크기 N
A = list(map(int, input().split()))

A.sort()

mid = A[(len(A) - 1) // 2]
result = [mid]

cnt = A.count(mid)

for _ in range(cnt):
    A.remove(mid)

cnt = len(A)

for _ in range(cnt):
    length = len(A)
    if length == 0:
        break

    criterion = A[(length - 1) // 2]            # 정렬된 배열 A의 중간값을 기준으로 삼음 
    
    i = binary_search2(A, criterion, 0, length - 1, 0, (length - 1) // 2)

    if A[i] in result:
        A.pop(i)
        continue
    else:    
        result.append(A[i])
        A.pop(i)
    
print(len(result))
"""