# SWEA 24.08.09.(금) - 1224. [S/W 문제해결 기본] 6일차 - 계산기3 (D4)

import sys
import operator

sys.stdin = open('sample_input\sample_input(33).txt', 'r')

# 후위 표기법으로 수정하는 함수
def toPostfix(string):
    global operators

    formula = list(string)
    my_stack = []               # 연산자 (임시) 저장 스택
    result_stack = []           # 후위표기법 식 저장 스택

    # 1. 후위 표기법으로 수정
    for token in formula:
        # 토큰이 여는 괄호인 경우
        if token == '(':
            my_stack.append(token)
        # 토큰이 연산자인 경우
        elif token in operators:
            # 토큰이 스택의 top에 저장되어 있는 연산자보다 우선순위가 높으면
            if not my_stack or (operators[token][1] < operators[my_stack[-1]][1]):
                # 스택에 push함
                my_stack.append(token)
            # 토큰이 스택의 top에 저장된 연산자보다 우선순위가 낮거나 같으면
            else:
                while len(my_stack) > 0 and operators[my_stack[-1]][1] <= operators[token][1]:
                    result_stack.append(my_stack.pop())      # stack에 있는 연산자를 pop 하여 결과식에 포함함
                my_stack.append(token)
        # 토큰이 닫는 괄호인 경우
        elif token == ')':
            poped = my_stack.pop()
            while poped != '(':
                result_stack.append(poped)
                poped = my_stack.pop() 
        # 토큰이 피연산자인 경우
        else:
            result_stack.append(int(token))
    
    for _ in range(len(my_stack)):
        result_stack.append(my_stack.pop())
        
    return result_stack


# 후위 표기법 식 계산 함수
def calPostfix(lst):
    global operators

    my_stack = []

    for l in lst:
        # 연산자인 경우
        if l in operators:
            ope = operators[l][0]

            y = my_stack.pop()
            x = my_stack.pop()

            my_stack.append(ope(x, y))
        # 피연산자인 경우
        else:
            my_stack.append(l)
    return my_stack.pop()

            
# 연산자 메서드와 연산자 우선순위 정보
operators = {'+': [operator.add, 2], 
            '-': [operator.sub, 2], 
            '*': [operator.mul, 1], 
            '/': [operator.truediv, 1],
            '(':[None, 3]
            }


T = 10

for tc in range(1, T + 1):
    N = int(input())            # 문자열의 계산식 길이
    string = input()

    # 1. 입력된 식을 후위 표기법으로 수정
    result_lst = toPostfix(string)
    
    # 2. 후위 표기법 식 계산
    result = calPostfix(result_lst)

    print(f'#{tc} {result}')