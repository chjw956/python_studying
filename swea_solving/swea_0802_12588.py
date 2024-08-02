# SWEA 12588. 4864. [파이썬 S/W 문제해결 기본] 3일차 - 문자열 비교 (D2)

import sys
sys.stdin = open('sample_input\sample_input(13).txt', 'r')

T = int(input())

for test_case in range(T):
    str1 = input()
    str2 = input()

    N = len(str1)
    M = len(str2)

    exist = 0

    for idx in range(M):
        if str2[idx] == str1[0]:
            if str2[idx:idx + N] == str1:
                exist = 1
                break
    
    print(f'#{test_case +1} {exist}')