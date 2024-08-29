# SWEA 24.08.29.(목) - 5186. [파이썬 S/W 문제해결 구현] 1일차 - 이진수2 (D2)
# 0보다 크고 1미만인 십진수 N을 이진수로 바꿀 때, 
# N을 소수점 아래 12자리 이내인 이진수로 표시할 수 있으면 0.을 제외한 나머지 숫자를 출력하고,
# 13자리 이상인 경우에는 'overflow'를 출력하는 프로그램

import sys
sys.stdin = open('sample_input\sample_input(45).txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N = float(input())
    result = ''
    cnt = 0
    exponent = -1

    print(f'#{tc}', end = ' ')

    while N != 0:
        if cnt > 12:
            print('overflow')
            break
        cnt += 1
        
        result += str(int(N // (2 ** exponent)))
        N %= 2 ** exponent
        exponent -= 1

    if cnt > 12:
        continue
    
    print(result)