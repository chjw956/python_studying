# SWEA 1209. [S/W 문제해결 기본] 2일차 - Sum (D3)
# 100 x 100의 2차원 배열에서 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값을 출력

import sys
sys.stdin = open('sample_input(7).txt', 'r')

"""
# append()와 sort()를 버무린 구린 코드 버전
for _ in range(10):
    test_case = int(input())

    matrix = []
    row_sums = []
    col_sums = []
    diagonal_sums = []

    for _ in range(100):
        row = list(map(int, input().split()))
        matrix.append(row)
        
        # 각 행의 합 리스트 생성
        row_sum = 0
        for r in row:
            row_sum += r
        row_sums.append(row_sum)

    to_right_diagonal = 0
    to_left_diagonal = 0

    # 각 열의 합 리스트 생성
    for c in range(100):
        col_sum = 0
        
        for r in range(100):
            col_sum += matrix[r][c]
            # 대각선의 합 구하기
            if c == r :
                to_right_diagonal += matrix[r][c]
            if c + r == 99:
                to_left_diagonal += matrix[r][c]
        col_sums.append(col_sum)
    
    diagonal_sums.append(to_left_diagonal)
    diagonal_sums.append(to_right_diagonal)

    row_sums.sort()
    col_sums.sort()
    diagonal_sums.sort()

    to_compare = []

    to_compare.append(row_sums.pop())
    to_compare.append(col_sums.pop())
    to_compare.append(diagonal_sums.pop())

    to_compare.sort()

    print(f'#{test_case} {to_compare[-1]}')
"""

# 강사님 피드백대로 append()와 sort()를 제거한 버전
for _ in range(10):
    test_case = int(input())

    matrix = []
    to_compare =[]

    # mx sum을 함부로 0으로 초기화하면 안됨
    # 문제 조건을 보고 초기화 조건을 생각하기!
    mx_row_sum = - 2 ** 16            # '각 행의 합은 integer 범위를 넘어가지 않는다!'
    mx_col_sum = - 2 ** 16

    for _ in range(100):
        row = list(map(int, input().split()))
        matrix.append(row)
        
        row_sum = 0

        for r in row:
            row_sum += r
        
        if row_sum > mx_row_sum:
            mx_row_sum = row_sum

    to_right_diagonal = 0
    to_left_diagonal = 0

    for c in range(100):
        col_sum = 0
        
        for r in range(100):
            col_sum += matrix[r][c]
            # 대각선의 합 구하기
            if c == r :
                to_right_diagonal += matrix[r][c]
            if c + r == 99:
                to_left_diagonal += matrix[r][c]
        if col_sum > mx_col_sum:
            mx_col_sum = col_sum
    
    to_compare.append(to_left_diagonal)
    to_compare.append(to_right_diagonal)
    to_compare.append(mx_row_sum)
    to_compare.append(mx_col_sum)

    to_compare.sort()

    print(f'#{test_case} {to_compare[-1]}')