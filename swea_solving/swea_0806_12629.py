# SWEA 12629. 4866.[파이썬 S/W 문제해결 기본] 4일차 - 괄호검사 (D2)
# 정훈이가 알려줌!

import sys
sys.stdin = open('sample_input\sample_input(19).txt', 'r')

T = int(input())

str_pair = {'(':')', '{':'}'}

for test_case in range(T):
    input_str = input()
    my_stack = []
    top = -1
    for i in range(len(input_str)):
        if input_str[i] in str_pair:
            top += 1
            my_stack.append(input_str[i])

        if input_str[i] == ')' or input_str[i] == '}':
            if top < 0 or str_pair[my_stack[top]] != input_str[i]:
                print(f'#{test_case + 1} 0')
                break
            else:
                top -= 1
                my_stack.pop()
    
        if i == len(input_str) - 1: 
            if top == -1:
                print(f'#{test_case + 1} 1')
            else:
                print(f'#{test_case + 1} 0')