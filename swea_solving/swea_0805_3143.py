# SWEA 3143. 가장 빠른 문자열 타이핑 (D4)
# A와 B가 주어질 때 A 전체를 타이핑하기 위해 키를 눌러야 하는 횟수의 최소값을 구하라.

# testpytestpythontesttestest test 와 같이 겹치는 문자가 있을 때의 탐색 결과에 유의해야 함

import sys
sys.stdin = open('sample_input\sample_input(16).txt', 'r')

T = int(input())

for test_case in range(T):
    A, B = input().split()

    len_A = len(A)
    len_B = len(B)

    same_idx = []

    idx = 0                             # 시작점 설정

    while idx < len_A:
        cnt = 0
        for (a, b) in list(zip(A[idx : idx + len_B], B)):
            if a != b:
                break
            else:
                cnt += 1
        if cnt == len_B:
            same_idx.append(idx)
            idx += len_B
        else:
            idx += 1


    total = (len_A - len(same_idx) * len_B) + len(same_idx)

    print(f'#{test_case + 1} {total}')