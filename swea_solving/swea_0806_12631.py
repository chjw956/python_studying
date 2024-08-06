# SWEA 12631. 4873. [파이썬 S/W 문제해결 기본] 4일차 - 반복문자 지우기 (D2)
import sys
sys.stdin = open('sample_input\sample_input(18).txt', 'r')

def sameThingIdx(lst):
    if len(lst) <= 1:
        return -1
    for i in range(len(lst) - 1):
        if lst[i] == lst[i+1]:
            return i
    return -1


def removeSame(lst):
    idx = sameThingIdx(lst)
    # 같은 것이 존재한다면
    if idx != -1:
        lst = lst[:idx]+lst[idx+2:]
        return removeSame(lst)
    # 존재하지 않는다면
    elif idx == -1:
        rslt = ''.join(lst)
        return rslt


T = int(input())

for test_case in range(T):
    input_lst = list(input())
    idx = sameThingIdx(input_lst)

    result = removeSame(input_lst)

    print(f'#{test_case + 1} {len(result)}')

