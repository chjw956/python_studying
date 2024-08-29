# SWEA 24.08.29.(목) - 5185. [파이썬 S/W 문제해결 구현] 1일차 - 이진수 (D2)
# N자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표시하는 프로그램을 만드시오.
# 단 2진수의 앞자리 0도 반드시 출력한다.

import sys
sys.stdin = open('sample_input\sample_input(46).txt', 'r')


def deciTobi(n):
    rslt = []

    while n != 0:
        rslt.insert(0, n % 2)
        n //= 2

    return rslt


hexadecimal = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


T = int(input())

for tc in range(1, T + 1):
    N, value = input().split()
    N = int(N)
    num = 0
    deci = 0
    result = ''

    for i in range(len(value)):
        # 1. 십진수로 변경
        # 숫자가 아니라면
        if not value[i].isdigit():
            deci =  hexadecimal[value[i]]
        else:                   # 숫자라면
            deci = int(value[i])

        # 2. 이진수로 변경
        rslt = deciTobi(deci)
        result += ''.join(str(r) for r in rslt).zfill(4)
        
    print(f'#{tc} {result}')        