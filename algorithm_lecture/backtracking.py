# 백트래킹을 이용해 {1, 2, 3, 4}에 대한 순열 생성
# 순열
def backtracking_perm(empty, length):
    if len(empty) == length:
        print(empty, end = ' ')
        return empty
    
    for i in range(len(array)):
        if used[i] == False:
            used[i] = True
            backtracking_perm(empty + [array[i]], length)
            used[i] = False


# 조합
def backtracking_comb(empty, length, idx):
    if len(empty) == length:
        print(empty, end = ' ')
        return empty
    
    for i in range(idx + 1, len(array)):
        if used[i] == False:
            used[i] = True
            backtracking_comb(empty + [array[i]], length, i)
            used[i] = False


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
length = 3
used = [False for i in range(len(array))]

backtracking_perm([], length)
print()
backtracking_comb([], length, -1)