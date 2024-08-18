# 백준 12015. 가장 긴 증가하는 부분 수열2 (G2)
# criterion(기준)값보다 작은 값 중에 가장 작은 값을 순차적으로 출력


def binary_search2(array, target, start, end, difference, idx):
    while start <= end:
        mid = (start + end) // 2
        
        if target - array[mid] <= difference:
            end = mid - 1
        else:
            start = mid + 1
        idx = mid
    return idx


N = int(input())        # 수열의 크기 N
A = list(map(int, input().split()))

mid = A[(N - 1) // 2]
result = [A[0]]
i = -1                   # 시작점

for _ in range(N):
    i += 1
    
    criterion = A[0]            
    
    i = binary_search2(A, criterion, i, N - 1, 0, (N - 1) // 2)

    if A[i] not in result and result[-1] < A[i]:
        result.append(A[i])
    
    if i == N - 1:
        break

print(result)
print(len(result))

