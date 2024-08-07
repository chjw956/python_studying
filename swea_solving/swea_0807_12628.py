# SWEA 24.08.07.(수) 12628. 4869.[파이썬 S/W 문제해결 기본]4일차 - 종이붙이기
# 점화식!
# 재귀함수나 메모이제이션으로 풀면 된다고 함!

import sys
sys.stdin = open('sample_input\sample_input(21).txt', 'r')

# 재귀 함수 -> 시간이 많이 걸림
def recursion(n):
    # memorize
    global memo

    if n >= 2:
        memo[n] =  2 * recursion(n - 2) + recursion(n - 1)
    
    return memo[n]

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    n = N // 10
    memo = [0] * N

    memo[0] = 1
    memo[1] = 1

    print(f'#{test_case}', end = ' ')
    print(recursion(n))