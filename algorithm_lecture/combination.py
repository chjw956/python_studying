arr = ['A', 'B', 'C', 'D', 'E']

# for문으로 구현
# for i in range(len(arr)):
#     start1 = i + 1
#     for j in range(start1, len(arr)):
#         start2 = j + 1
#         for k in range(start2, len(arr)):
#             print(arr[i], arr[j], arr[k])



path = []
n = 3


def run(lev, start):
    if lev == n:
        print(path)
        return
    
    for i in range(start, len(arr)):
        path.append(arr[i])
        run(lev + 1, i + 1)             # 재귀 호출
        path.pop()


run(0, 0)
