"""
# 부분집합 합(Subset Sum) (24.07.31. 수업 내용)
# 연습 문제 

- 9개의 정수를 입력 받아 부분집합의 합이 0이 되는 것이 존재하는지를 계산하는 함수를 작성해보자.
- 입력 값: -7 -5 2 3 8 -2 4 6 9

# 강사님 풀이 10시 50분 넘어서
# 나는 부분집합의 합이 0이 되는 것들을 반환함

"""
from pprint import pprint
# import sys

input_lst = list(map(int, input().split()))
bit_maps = []
subsets = []
zero_subsets = []

# 비트맵 개념 사용
N = len(input_lst)                                   # n : 원소의 개수

if __name__ == '__main__' :
    # 부분 집합의 개수만큼 반복
    for i in range(1 << N):                 # 1 << n : 부분 집합의 개수
        bit_map = []
        subset = []
        for j in range(N-1, -1, -1):        # 원소의 수만큼 비트를 비교함
            if i & (1 << j):                # i의 j번째 비트가 1이라면
                bit_map.append(1)
                subset.append(input_lst[j])
            else:
                bit_map.append(0)
        bit_maps.append(bit_map)
        
        if subset != [] and sum(subset) == 0:
            zero_subsets.append(subset)
        
    # print(False)
    pprint(zero_subsets)
