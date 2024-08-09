# SWEA 24.08.09.(금) 4875.[파이썬 S/W 문제해결 기본] 5일차 - 미로 (D2)

import sys
sys.stdin = open('sample_input\sample_input(23).txt', 'r')

def backtracking(matrix, s, g, n):
    positions = [s]         # 스택
    
    for i in range(n - 1, -1, -1):
        


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    matrix = []
    start = [-1, -1]
    goal = [-1, -1]

    for n in range(N):
        line = list(map(int, input().split()))
        if 2 in line:
            start = [n, line.index(2)]
        
        if 3 in line:
            goal = [n, line.index(3)]

        matrix.append(line)



    
