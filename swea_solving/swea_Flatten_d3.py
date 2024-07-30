"""
제한된 횟수만큼 옮기는 작업을 수행한 후 최고점과 최저점의 차이를 반환하는 알고리즘
평탄화를 모두 수행하고 나면, 가장 높은 곳과 가장 낮은 곳의 차이가 최대 1 이내가 됨

'덤프': 가장 높은 곳에 있는 상자를 가장 낮은 곳으로 옮기는 작업

-> 즉 평탄화과 완료되면 최대 차이가 1 이내이지만, 완료되지 않은 채로 제한된 횟수가 종료될 수 있다는 뜻이네!
"""

import sys
sys.stdin = open('sample_input(4).txt', 'r')


def dump(lst, n):
    dump_num = 0

    for _ in range(n):
        lst.sort(reverse = True)

        if lst[0] - lst[-1] <= 1:
            return lst[0] - lst[-1]
        
        lst[0] -= 1
        lst[-1] += 1
        dump_num += 1
    
    lst.sort(reverse = True)

    return lst[0] - lst[-1]


for test_case in range(10):
    N = int(input())            # 덤프 횟수
    height_list = list(map(int, input().split()))
    
    result = dump(height_list, N)

    print(f'#{test_case + 1} {result}')