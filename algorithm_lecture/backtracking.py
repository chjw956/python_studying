# 백트래킹을 이용해 {1, 2, 3, 4}에 대한 순열 생성
# 순열
def backtracking(arr, k):
    if len(arr) == k:
        print(arr, end = ' ')
        return arr
    
    for i in range(len(array)):
        if used[i] == False:
            used[i] = True
            backtracking(arr + [array[i]], k)
            used[i] = False


# 조합
def backtracking_comb(arr, k, idx):
    if len(arr) == k:
        print(arr, end = ' ')
        return arr
    
    for i in range(idx + 1, len(array)):
        if used[i] == False:
            used[i] = True
            backtracking_comb(arr + [array[i]], k, i)
            used[i] = False


array = [1, 2, 3, 4]
k = 2
used = [False for i in range(len(array))]

backtracking([], k)
print()
backtracking_comb([], k, -1)