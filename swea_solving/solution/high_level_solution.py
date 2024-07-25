"""
모든 문제를 DFS로 풀 수 있으면 좋겠지만, 그리고 itertools 라이브러리를 쓸 수 있으면 좋겠지만,
최악의 상황에서의 문제는 그렇지 않고 아래와 같은 조합 문제도 중요하다.

트리나 그래프가 아니어도 재귀적으로 스택을 활용해서 안쪽으로 파고들어서 해를 구하는 과정을 모두 DFS라고 표현한다.
"""
"""
모든 조합의 경우의 수를 구함 => subset(부분집합), 부분집합의 시간복잡도: O(2^n)
문제에서 N의 최대값이 20이었으므로 => 2^20 = 1024 * 1024 = 약 100만 (조합으로 충분히 구현 가능한 수준)
"""
"""
* DFS로 했을 때 속도가 빨라진 이유
: 기존의 조합 + 재귀 방식에서는 슬라이싱 해서 넘기는 부분과 리스트를 합쳐서 메모리가 확장되는 과정에서 
시간복잡도가 좀 올라감. 그러나 DFS에서는 그 과정이 사라졌기 때문에 시간이 줄어든 것!
+) 조합보다는 DFS를 사용하는 것이 빠른 이유가, DFS는 문제의 조건에 따라 유연하게 추가하여 가지치기가 가능하지만 
조합은 모든 경우의 수를 다 구해야 하기 때문임.
"""
"""
모든 조합을 구하는 것 == 부분 집합을 구하는 것!
부분집합을 가장 간단하게 구현하는 방법: 비트마스크 활용하는 것!
"""
"""
비트마스크 활용한 비트 연산 방법이 훨씬 빠른 이유?
1. 비트 연산은 CPU에서 직접 처리되므로 저수준 연산이다 따라서 매우 빠름
2. 정수 하나로 부분집합을 표현하므로 메모리 접근을 최소화한다.

하지만 itertools를 이길 수는 없다.
"""
"""
itertools가 압도적인 시간차를 보이는 이유?
1. 내부 구현이 C이므로 파이썬 코드보다 빠름
2. generator를 활용 (모든 조합을 한번에 생성하지 않고, 필요할 때마다 생성함)
 -> 따라서 대량의 객체를 만들지 않아 오버헤드도 없고 빠른 속도를 보인다.
    또한 필요할 때마다 생성하므로 작은 단위로 데이터를 처리하므로 CPU 캐시를 효율적으로 사용한다.
3. 내장함수의 인터프리터에 의해 최적화되고, 알고리즘 자체도 극한으로 최적화되어 있음.
"""
"""

"""


import sys
sys.stdin = open('input4.txt')

import time                                 # 시간 측정이 필요할 때 사용하면 좋은 모듈
from itertools import combinations          # itertools 사용하니까 0.03 초 나옴....


# 재귀로 구현
def get_combinations_recur(arr, n):
    result = []                 # 결과를 저장할 빈 리스트 초기화

    if n == 1:                  # 선택할 요소가 1개인 경우, 각 요소 자체가 하나의 조합이 된다.
        return [[i] for i in arr]
    
    for i in range(len(arr)):
        elem = arr[i]           # i번째 요소를 고정시켜 두고
        # 현재 고정시켜 둔 요소 다음부터 재귀로 넘김
        # 또한 한 개를 이미 골랐으므로, 다음 재귀로 넘길 때에는 한 개를 빼서 넘김
        for rest in get_combinations_recur(arr[i+1:], n-1):
            result.append([elem] + rest)

    return result               # 최종 조합 결과 반환

# DFS로 구현
def get_combinations_dfs(arr, n):
    result = []             # 조합 목록을 저장하는 변수

    # dfs를 구현할 함수
    # dfs 안에 재귀의 개념이 들어갔던가...ㅎ;
    def get_comb(start, comb):
        if len(comb) == n:      # 여태까지 선택한 조합의 목록이 우리가 원하는 조합의 개수에 도달하면
            result.append(comb[:])

        # 파라미터로 건네진 start(시작점)부터 총 개수까지 순회함
        for i in range(start, len(arr)):
            comb.append(arr[i])         # 선택하고
            get_comb(i + 1, comb)       # 선택한 것 다음부터 다시 선택을 해야 하므로, 시작 지점을 +1 해서 넘김.
            comb.pop()                  # 해당 선택지는 종료되었고, 다른 선택지를 골라야 하므로 최근에 선택했던 것을 추출


    # 부분 집합 했을 때, 하나의 원소를 선택했다고 치고, 그 다음 위치의 인덱스부터 다시 하나를 선택하는 것!
    # 현재 선택해야 하는 원소의 위치(start)와 여태까지 선택된 조합의 목록(comb)을 넘김
    get_comb(0, [])
    return result

start_time = time.time()
T = int(input())


# 완전 탐색으로 구현
for test_case in range(1, T+1):
    N, B = map(int, input().split())
    arr = list(map(int, input().split()))
    res = float('inf')

    def get_min_tower_height(N, B, heights):
        min_height = float('inf')           # 조합을 구현하고, 최소값을 찾으면 최소값으로 갱신함

        # height(N) 명에 대해 1명을 선택하는 것부터, N명 모두를 선택하는 조합을 모두 구한 후에
        # 그 조합들의 합을 구하고, 거기서 B를 넘는 것 중에 가장 적은 수를 구하기
        for r in range(1, N+1):

            # heights(직원들의 키 리스트)에서 r명을 선택한 조합 (완전 탐색, 재귀)
            # for comb in get_combinations_recur(heights, r):

            # dfs 이용
            # for comb in get_combinations_dfs(heights, r):
            for comb in combinations(heights, r):
                total_height = sum(comb)        # 직원들 조합의 모든 키를 합한 값

                # 점원들의 합이 탑의 높이와 같아지면, 더이상 조합을 구할 필요가 없다.
                # 조합과 재귀의 방식으로 접근할 때 이런 조건을 추가해주는 것이 시간을 줄이는 데 매우 효율적임
                # 가지치기 혹은 백트래킹이라고 함 (조건을 만족하면 중간에 빠져나오는 것)
                if total_height == B:
                    return B

                # B보다 크거나 같으면 최소값을 갱신함
                if total_height >= B:
                    min_height = min(min_height, total_height)

        return min_height
    
    # 비트마스크 활용 skeleton 코드
    def get_subsets_bitmask():
        global res
        # 로직 #
        # 비트를 1비트 만큼 옆으로 옮겨가면서 그 개수를 비교해서
        # 각 위치마다 포함하느냐 안 하느냐로 계산하는 것!
        # 따라서 부분집합의 개수만큼 for loop를 반복해야 한다.

        subset_cnt = 2 ** N

        # 모든 경우의 수를 순회하는 것
        for i in range(1, subset_cnt):      # i에 해당하는 숫자들을 비트로 바꿔서 비트 연산할 것임
            """
            001
            010
            011
            100
            101
            """
            
            h_sum = 0
            for j in range(N):
                if i & (1 << j):
                    h_sum += arr[j]
            
            if h_sum >= B:
                res = min(res, h_sum)

        return 

    # 완전 탐색 또는 DFS로 구하는 코드
    # res = get_min_tower_height(N, B, arr)

    # 비트마스크 활용 코드
    # get_subsets_bitmask()
    
    print(f"#{test_case} {res - B}")

end_time = time.time()
print("실행 시간: ", end_time - start_time)