# 24.08.01.(목) [라이브 강의] 알고리즘 list2
# 델타 활용 연습문제

# 2차 배열을 정렬하여 출력하라.

from pprint import pprint

arr = [[9, 20, 2, 18, 11],
       [19, 1, 25, 3, 21],
       [8, 24, 10, 17, 7],
       [15, 4, 16, 5, 6],
       [12, 13, 22, 23, 14]]

len_arr = len(arr)

# 우 하 좌 상
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
move = list(zip(di, dj))

for i in range(1, len_arr):
    arr[0] += arr[i]
    arr[i] = [0] * len_arr

arr[0].sort()

i = 0
# m = j = len_arr - 1이라고 두면 같은 주소값을 가지게 되어서 m 값을 변경했을 때 j 값도 변경되나?
j = m = len_arr - 1         # 4
cnt = 1

while m > 0:
    for _ in range(2):
        for __ in range(m):
            i += move[cnt][0]
            j += move[cnt][1]
            arr[i][j] = arr[0][len_arr]
            arr[0].pop(len_arr)
        if cnt >= 3:
            cnt = 0
        else:
            cnt += 1
    m -= 1   

pprint(arr)