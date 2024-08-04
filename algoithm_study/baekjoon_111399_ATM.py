# 백준 11399번 ATM (silver 4)
"""
각 사람이 돈을 인출하는 데 필요한 시간이 최솟값이 되어야
전체 필요 시간 또한 최솟값이 되므로,
이것은 정렬을 이용해야 함을 알 수 있다(?)고 생각함

"""


# 선택정렬
def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(len(arr[i:])):
            if arr[min_idx] > arr[j + i]:
                min_idx = j + i
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


N = int(input())
times = list(map(int, input().split()))

result = selectionSort(times)
time = 0

for i, r in enumerate(result):
    time += r * (N - i) 

print(time)