# 24.08.06.(화) [재귀 호출] 모든 배열 원소에 접근하기

arr = ['a', 'b', 'c']

def f(i, N):
    if i == N:
        return
    else:
        print(arr[i])
        f(i + 1, N)

f(0, 3)