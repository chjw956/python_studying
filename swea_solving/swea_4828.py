import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

for test_case in range(T):
    N = int(input())
    A = list(map(int, input().split()))

    min = A[0]
    max = A[0]

    for a in A:
        if a > max:
            max = a

        if a < min:
            min = a

    print(f'#{test_case + 1} {max - min}')
