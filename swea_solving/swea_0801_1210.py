# SWEA 1210.[S/W 문제해결 기본] 2일차 - Ladder1
import sys
sys.stdin = open('sample_input(11).txt', 'r')

for _ in range(1):
    test_case = int(input())

    matrix = []
    entrances = []
    idx = 0

    first = list(map(int, input().split()))
    matrix.append(first)
    print(first)

    # print(first.count(1))
    # for _ in range(first.count(1)):
    #     idx = first[idx + 1:].index(1)
    #     print(idx)
    #     entrances.append(2 * idx + 1)

    for i in range(1, 100):
        matrix.append(list(map(int, input().split())))
        
    # print(f'entrances = {entrances}')

        
