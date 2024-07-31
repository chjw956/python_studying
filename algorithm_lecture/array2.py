"""
# 배열 2 (24.07.31. 수업 내용)
# 연습 문제 

1. 5x5 2차원 배열에 25개의 숫자를 저장하고 대각선 원소의 합을 구하시오.
2. 각 요소에 대해서 그 요소와 이웃한 요소와의 차의 절대값의 합을 구하시오. 
3. 25개 요소에 대해 모두 조사하여 절대값의 총합을 구하시오.

# 영상에서 10시 20분쯤 해당 문제 풀어주심

"""
from pprint import pprint

# 나의 풀이
N = 5
matrix = []

# 5x5 2차원 배열 생성
for i in range(N):
    lst = []
    for j in range(i * 5 + 1, i * 5 + 6):
        lst.append(j)
    matrix.append(lst)

# 대각선 원소의 합 구하기
diagonal_sum = 0

for i, m in enumerate(matrix):
    for j, n in enumerate(m):
        if i == j or i + j == 4:
            diagonal_sum += n

# 요소와 이웃한 요소와의 차의 절대값의 합 구하기
# 방향별로 더할 값
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

index_d = list(zip(di, dj))

abs_sum = 0
abs_list = []

for i, m in enumerate(matrix):
    for j, n in enumerate(m):
        abs_v = 0
        for d in index_d:
            if 0 <= i + d[0] < N and 0 <= j + d[1] < N:
                abs_v += abs(n - matrix[i + d[0]][j + d[1]])
                # print(f'n = {n}, abs_v = {abs_v}')
        abs_list.append(abs_v)
        # 절대값의 총합 구하기
        abs_sum += abs_v

print(f'abs_sum = {abs_sum}')