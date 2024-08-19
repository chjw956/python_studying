# SWEA 24.08.09.(금) 4875.[파이썬 S/W 문제해결 기본] 5일차 - 미로 (D2)
# N * N 크기의 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인하는 프로그램 (경로 있으면 1, 없으면 0 출력)

import sys
sys.stdin = open('sample_input\sample_input(23).txt', 'r')

"""
# 강사님이 짜주신 코드
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

"""

from collections import deque


# BFS 메서드 정의 (동빈나 버전을 간선 개수 구하기 쉽게 변형)
def BFS(graph, start, visited):
    # 1. 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])

    # 2. 현재 노드 방문 처리
    num = 1
    visited[start] = num

    # 3. 큐가 빌 때까지 반복
    while queue:
        # 3-1. 큐에서 하나의 원소를 뽑음 (deque())
        v = queue.popleft()

        # 3-2. 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입하고 방문 처리함
        for i in graph[v]:
            if not visited[i]:
                num += 1
                queue.append(i)
                visited[i] = num



# Runtime Error 나는데 왜 나는지 모르겠음

def BFS_modified(graph, si, sj, visited, n):
    # 1. 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([[si, sj]])

    # 2. 현재 노드 방문 처리
    num = 1
    visited[si][sj] = num

    # 상 하 좌 우
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    # 3. 큐가 빌 때까지 반복
    while queue:
        # 3-1. 큐에서 하나의 원소를 뽑음 (deque())
        v = queue.popleft()

        # 3-2. 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입하고 방문 처리함
        for d in directions:
            di = v[0] + d[0]
            dj = v[1] + d[1]

            if 0 <= di < n and 0 <= dj < n and not visited[di][dj]:
                if graph[di][dj] == 3:
                    return 1
                
                if graph[di][dj] == 0:
                    num += 1
                    queue.append([di, dj])
                    visited[di][dj] = num
                
    return 0


def findStart(matrix, START):
    si = sj = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == START:
                si, sj = i, j

    return si, sj


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    START = 2
    TARGET = 3

    matrix = []

    for _ in range(N):
        matrix.append(list(map(int, input())))

    visited = [[0] * N for _ in range(N)] 

    # 출발점 찾기
    si, sj = findStart(matrix, START)

    result = BFS_modified(matrix, si, sj, visited, N)

    print(f'#{tc} {result}')