# BAEKJOON 2075. N번째 큰 수 (silver2)
# 제한 시간: 1초
# N x N 의 표에 채워진 N^2의 수에 대해 각 자리의 수는 자신의 한 칸 위 수보다 큰 값을 갖는다.
# 즉, 열 단위로 오름차순의 값을 가진다.
# 이때, N번째 큰 수를 찾아 출력하라.
# 메모리 초과남..;;

import sys
sys.stdin = open('sample_input\sample_input(18).txt', 'r')


"""
# 메모리 초과 1

from heapq import heappush, heappop

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)]

max_heap = []

# 완탐
for i in range(N):
    for j in range(N):
        heappush(max_heap, (-table[i][j], table[i][j]))

cnt = 1
while cnt <= N:
    minus_value, value = heappop(max_heap)
    cnt += 1

print(value)

"""


"""
# 메모리 초과 2
from heapq import nlargest

N = int(input())
values = []
for _ in range(N):
    values += list(map(int, input().split()))
print(nlargest(N, values)[-1])

"""

# 이번엔 시간초과..^^
from queue import PriorityQueue

N = int(input())
q = PriorityQueue(maxsize = N)

for _ in range(N):
    for n in list(map(int, input().split())):
        if q.full():
            q.get()
            q.put(n)
        else:
            q.put(n)

print(q.get())