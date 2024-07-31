# SWEA 12497. 2일차 - 색칠하기 (D2)

import sys
from pprint import pprint 

# sys.stdin = open('sample_input(5).txt', 'r')
sys.stdin = open('sample_input(5).txt', 'r')

PURPLE = 3
T = int(input())
L = 10

for test_case in range(T):
    N = int(input())
    colors = []
    cnt = 0

    for _ in range(N):
        colors.append(list(map(int, input().split())))
    
    matrix = []
    for _ in range(L):
        lst = []
        for __ in range(L):
            lst.append(0)
        matrix.append(lst)

    for c in colors:
        for i in range(L):
            for j in range(L):
                if c[0] <= i <= c[2] and c[1] <= j <= c[3]:
                    matrix[i][j] += c[4]
                    if matrix[i][j] == 3:
                        cnt += 1
    
    # pprint(matrix)
    print(f'#{test_case + 1} {cnt}')
    
        