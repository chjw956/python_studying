# 백준 11651. 좌표 정렬하기2 (Silver 2)
"""
N = int(input())

coordinates = []

for _ in range(N):
    x, y = map(int, input().split())
    coordinates.append((x, y))

coordinates.sort(key=lambda x:(x[1], x[0]))            # 좌표를 y가 증가하는 순으로 정렬

for (x, y) in coordinates:
    print(f'{x} {y}')


"""


# 다른 방법으로 풀기

# y값 기준 선택 정렬
def selectSort2(lst):
    length = len(lst)
    for i in range(length):
        small_idx = i
        for j in range(i + 1, length):
            if lst[small_idx][1] > lst[j][1]:
                small_idx = j
            elif lst[small_idx][1] == lst[j][1]:
                if lst[small_idx][0] > lst[j][0]:
                    small_idx = j
        lst[small_idx], lst[i] = lst[i], lst[small_idx]
    
    return lst


N = int(input())

coordinates = []

for _ in range(N):
    x, y = map(int, input().split())
    coordinates.append((x, y))

# y값 기준 정렬
coordinates = selectSort2(coordinates)

for (x, y) in coordinates:
    print(f'{x} {y}')