# SWEA 12510.2일차 - 특별한 정렬 (D3) - 10개까지 출력하라고 함
import sys
sys.stdin = open('sample_input(10).txt', 'r')

T = int(input())

for test_case in range(T):
    N = int(input())
    num_list = list(map(int, input().split()))

    result = []

    # 완전 탐색
    while num_list != []:
        max_num = 1
        min_num = 100
        max_idx = 0
        min_idx = 0
        
        for idx, n in enumerate(num_list):
            if n > max_num:
                max_num = n
                max_idx = idx
            if n < min_num:
                min_num = n
                min_idx = idx    
        
        if max_idx > min_idx:
            result.append(num_list.pop(max_idx))
            result.append(num_list.pop(min_idx))
        elif max_idx < min_idx:
            result.append(num_list.pop(max_idx))
            result.append(num_list.pop(min_idx - 1))
        else:
            result.append(num_list.pop())

    print(f"#{test_case + 1} {' '.join(str(s) for s in result[:10])}")