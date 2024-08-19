# SWEA 24.08.08.(목) - 4874. [파이썬 S/W 문제해결 기본] 5일차 - Forth (D2)
# 후위 표기법 관련
# 1. 피연산자와 연산자를 어떻게 구분할 것인가
# 2. 연산자를 어떻게 실제 연산으로 연결시킬 것인가
# operator 모듈 쓰면 왜 안 되지?

import sys
import operator

sys.stdin = open('sample_input\sample_input(24).txt', 'r')

T = int(input())

operators = {'+': operator.add, 
            '-': operator.sub, 
            '*': operator.mul, 
            '/': operator.truediv
            }

for tc in range(1, T + 1):
    inputs = list(input().split())

    # 스택 생성
    my_stack = []

    print(f'#{tc}', end = ' ')

    for i in inputs:
        if i == '.':
            if len(my_stack) > 1 or not my_stack:
                print('error')
            else:
                print(my_stack.pop())
            break

        # 피연산자인 경우,
        if i not in operators:
            my_stack.append(int(i))
        # 연산자인 경우,
        else:
            if len(my_stack) < 2:
                print("error")
                break
            else:
                x = my_stack.pop()
                y = my_stack.pop()
                
                ope = operators[i]
                my_stack.append(ope(y, x))
                