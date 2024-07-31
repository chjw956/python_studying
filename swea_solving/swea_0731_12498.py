# SWEA 12498. 2일차 - 부분집합의 합 (D3)
# 집합 A의 부분 집합 중 N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 개수

import sys
from time import time
sys.stdin = open('sample_input(6).txt', 'r')

st_time = time()

arr = [i for i in range(1, 13)]
L = 12
T = int(input())

for test_case in range(T):
    N, K = map(int, input().split())

    subsets = []

    # N개의 원소를 가지는 부분집합만 만들기
    # 조합 문제네..
    
    for i in range(1 << L):
        subset = []
        for j in range(L):
            # 여기에서 조건을 달리 줘야 할 것 같은데..
            if i & (1 << j):
                subset.append(arr[j])
        
        if len(subset) == N and sum(subset) == K:
            subsets.append(subset)

    print(f'#{test_case + 1} {len(subsets)}')
end_time = time()
print(f'time = {end_time - st_time}')