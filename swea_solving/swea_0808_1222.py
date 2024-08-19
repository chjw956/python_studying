# SWEA 24.08.08. 1222. [S/W 문제해결 기본] 6일차 - 계산기1 (D4)

import sys
import operator

sys.stdin = open('sample_input\sample_input(31).txt', 'r')

T = int(input())

operators = {'+': operator.add, 
            '-': operator.sub, 
            '*': operator.mul, 
            '/': operator.truediv
            }

priority = [('*', 2), ('/', 2), ]