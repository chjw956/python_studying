# 24.08.06.(화) [재귀 호출] 배열에 v가 있으면 1, 없으면 0 리턴

def f(i, N, v):                 # v: 찾는 값
    if i == N:
        return 0
    elif arr[i] == v:
        return 1
    else:
        i += 1
        return f(i, N, v)

    
arr = ['a', 'b', 'c']

print(f(0, 3, 'c'))
print(f(0, 3, 'd'))