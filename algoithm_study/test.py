# N = int(input())

# for _ in range(N):
#     # tuple이 아니라 generator 객체로 생성됨
#     print(tuple((x, y) for x, y in map(int, input().split())))


# coordinate = tuple((x, y) for x, y in zip(map(int, input().split()[::2]), map(int, input().split()[1::2])))

# input_values = list(map(int, input().split()))

# coordinate = tuple((input_values[i], input_values[i+1]) for i in range(0, len(input_values), 2))


# lst = [1, 2, 3]

# lst.append(list(map(int, input().split())))
# print(lst)
# print(lst[-1:])


def spin(arr, w, h):
    spun = [[None for _ in range(w)] for __ in range(h)]

    print(spun)


array = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]

width = 4
height = 5


# 십자 모양 만들기!
toGo = []
idx1 = 2
idx2 = 1

i = 2
j = 1
power = 2

# for i in range(0, 3):
#     for j in range(0, 4):
#         if i == idx1 and [i, j] not in toGo:
#             toGo.append([i, j])
#         if j == idx2 and [i, j] not in toGo:
#             toGo.append([i, j])

for k in range(power + 1):
    if 0 <= i - k:
        toGo.append(array[i - k][j])
    if 0 <= j - k:
        toGo.append(array[i][j - k])
    if i + k < height:
        toGo.append(array[i + k][j])
    if j + k < width:
        toGo.append(array[i][j + k])


print(toGo)