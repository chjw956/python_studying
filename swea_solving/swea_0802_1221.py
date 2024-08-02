# SWEA 1221.[S/W 문제해결 기본] 5일차 - GNS (D3)
import sys
sys.stdin = open('sample_input\sample_input(14).txt', 'r')

T = int(input())

lst1 = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
lst2 = [0]* 10

for _ in range(T):
    L, N = map(int, input()[1:].split())
    input_list = list(input().split())
    numbers = dict(zip(lst1, lst2))

    for i in input_list:
        numbers[i] += 1
    
    num_values = list(numbers.items())

    result = ''

    print(f'#{L}')
    for (string, n) in num_values:
        for _ in range(n):
            result += string
            result += ' '
    print(result)

    