# BAEKJOON 27433번 팩토리얼2
# 재귀 함수 연습

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)


N = int(input())
print(factorial(N))
