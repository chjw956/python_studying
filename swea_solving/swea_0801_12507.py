# SWEA 12507. 2일차 - 이진탐색 D2
# 원래 이진탐색은 중간값을 버리고 이외의 부분을 새로운 집합으로 잡아서 탐색하는데,
# 이 문제는 중간값을 포함해서 새로운 집합을 만들라고 하고 있어서
# 무한 루프에 빠지게 될 가능성이 있다.

# 내 코드는 왜 무한 루프에 안 빠졌지?
# 어떤 조건 때문에?
import sys
sys.stdin = open('sample_input(8).txt', 'r')


def didYouFind(s, e, c, t, cnt):
    if c > t :
        e = c
    elif c < t:
        s = c
    elif c == t:
        return cnt
    
    cnt += 1
    return didYouFind(s, e, int((s + e) / 2), t, cnt)

T = int(input())

for test_case in range(T):
    total, Pa, Pb = map(int, input().split())
    c = int(total / 2)            # 중간 페이지

    findA = findB = False
    cnt = 0

    findA = didYouFind(1, total, c, Pa, cnt)
    findB = didYouFind(1, total, c, Pb, cnt)
    
    print(f'#{test_case + 1}', end=' ')
    if findA == findB:
        print(0)
    elif findA < findB:
        print('A')
    elif findA > findB:
        print('B')