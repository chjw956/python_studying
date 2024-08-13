# SWEA 24.08.09.(금) 4875.[파이썬 S/W 문제해결 기본] 5일차 - 미로 (D2)

# import sys
# sys.stdin = open('sample_input\sample_input(23).txt', 'r')


def is_safe(board, row, col, N):
    # 행 요소 하나하나 확인
    for i in range(col):
        if board[row][col] == 'Q':
            return False
    
    # 왼쪽 아래에서 오른쪽 위로의 대각선 체크
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False
    
    # 왼쪽 위에서 오른쪽 아래로의 대각선 체크
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    return True

def solve_n_queens(N):
    board = [['.' for _ in range(N)] for _ in range(N)]
    result = []

    def backtracking(board, col):
        if col == N:
            result.append([''.join(row) for row in board])
            return
        
        for i in range(N):
            if is_safe(board, i, col, N):
                board[i][col] = 'Q'
                backtracking(board, col + 1)
                board[i][col] = '.'
    backtracking(board, 0)
    return result


# Example 1
N1 = 4
result1 = solve_n_queens(N1)
print(f'Solution for Example 1 with N = {N1}: ')
for solution in result1:
    print(solution)
print()

# Example 2
N2  = 1
result2 = solve_n_queens(N2)
print(f'Solution for Example 2 with N = {N2}: ')
for solution in result2:
    print(solution)
print()


# def backtracking(matrix, s, g, n):
#     positions = [s]         # 스택
    
#     for i in range(n - 1, -1, -1):
        




# T = int(input())

# for tc in range(1, T + 1):
#     N = int(input())

#     matrix = []
#     start = [-1, -1]
#     goal = [-1, -1]

#     for n in range(N):
#         line = list(map(int, input().split()))
#         if 2 in line:
#             start = [n, line.index(2)]
        
#         if 3 in line:
#             goal = [n, line.index(3)]

#         matrix.append(line)



    
