# BAEKJOON 10870번 피보나치 수5
# 재귀 함수 연습

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 2) + fibonacci(n - 1)


N = int(input())
print(fibonacci(N))