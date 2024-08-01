# SWEA 1958.달팽이 숫자 D2
from pprint import pprint
import sys
sys.stdin = open('sample_input(9).txt', 'r')

T = int(input())

# 리스트 사용 (인덱스로 접근)
for test_case in range(T):
    N = int(input())
    matrix = []
    for i in range(N):
        lst = [0 for _ in range(N)]
        matrix.append(lst)
    
    # 우 하 좌 상
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    d = list(zip(di, dj))

    for n in range(1, N + 1):
        matrix[0][n - 1] = n

    i = 0
    m = 1
    j = N - 1
    num = N
    n = N + 1           # matrix에 넣을 숫자

    while num >= 1:
        # 횟수를 두 번씩 반복
        for _ in range(2):
            for __ in range(num - 1):
                i += d[m][0]
                j += d[m][1]
                matrix[i][j] = n
                n += 1
            if m == 3:
                m = 0
            else:
                m += 1
        num -= 1
    
    print(f'#{test_case + 1}')
    for m in matrix:
        print(' '.join(str(s) for s in m))