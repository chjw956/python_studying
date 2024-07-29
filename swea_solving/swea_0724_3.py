"""

import sys
sys.stdin = open('sample_input(1).txt', 'r')

T = int(input())

for test_case in range(T):
    N, M = map(int, input().split())
    m = (M - 1) // 2

    a_list = list(map(int, input().split()))

    sum_list = []
 
    for idx in range(m, N - m):
        # max = sum(a_list[0:(m + 1)])
        total = 0
        for j in range(m):
            total += a_list[j]
        
        min = max = total
        
        print(f'total = {total}')
        sum_v = 0

        for i in range(idx - m, idx + m + 1):
            if i >= 0 and i <= N - 1:
                sum_v += a_list[i]
        
        if sum_v > max :
            max = sum_v
        
        if sum_v < min:
            min = sum_v
    
    # sort 괘씸죄
    # sum_list.sort()

    # print(f'#{test_case + 1} {sum_list[-1] - sum_list[0]}')
    print(f'#{test_case + 1} {max - min}')
"""

# 나는 중심값을 두고 양쪽에 짝수개씩 나눠서 총 M개를 선택하는 걸로 했는데,
# 강사님은 그냥 시작점부터 + (M-1) 인덱스까지 더하는 걸로 접근하심


# 강사님 코드
# 반복해야 하는 횟수 : N - M + 1 번 -> 시간복잡도 관련인 건가?
# 반복을 위한 시작점 인덱스 범위는 range(0, N - M)이다.

import sys
sys.stdin = open('sample_input(1).txt', 'r')

T = int(input())

for test_case in range(T):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))

    max_sum = 1
    min_sum = 10000 * M

    # 인덱스 0번부터 N - M번까지 반복
    for i in range(N - M + 1):
        tmp_sum = 0
        for j in range(M):
            tmp_sum += numbers[i + j]
    
        if max_sum < tmp_sum:
            max_sum = tmp_sum
        
        if min_sum > tmp_sum:
            min_sum = tmp_sum

    print(f'#{test_case + 1} {max_sum - min_sum}')
