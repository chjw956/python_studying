# SWEA 12590. 4861.[파이썬 S/W 문제해결 기본] 3일차 - 회문 (D2)
# 회문 = Palindrome

import sys
sys.stdin = open('sample_input\sample_input(12).txt', 'r')

# 내가 짠 코드
def recursion(string, start, last):
    if start < 0 or last >= len(string):
        return 1, start + 1
    if string[start] != string[last]:
        return 0, start + 1
    else:
        return recursion(string, start -1, last + 1)
    

def isPalindrome(string):
    if len(string) % 2 == 0:
        return recursion(string, (len(string) - 2) // 2, (len(string) - 2) // 2 + 1)
    else:
        return recursion(string, (len(string) - 2) // 2, (len(string) + 1) // 2)


T = int(input())

for test_case in range(T):
    N, M = map(int, input().split())

    matrix = []
    palindrome_str = ''

    for n in range(N):
        line = input()
        matrix.append([i for i in line])

    # 행으로 존재하는 회목 문자열을 출력
    for i in range(N):              # 행의 수 결정
        for j in range(0, N - M + 1):           # 시작점 결정
            line = ''
            for m in range(j, j + M):
                # print(f'm = {m}')
                line += matrix[i][m]
            result, idx = isPalindrome(line)
            if result == 1:
                palindrome_str = line
                break
        if palindrome_str != '':
            break
                    
    if palindrome_str != '':
        print(f'#{test_case + 1} {palindrome_str}')
        continue

    # 열로 존재하는 회목 문자열 출력
    for j in range(N):
        for i in range(0, N - M + 1):
            line = ''
            for m in range(i, i + M):
                line += matrix[m][j]
            result, idx = isPalindrome(line)
            if result == 1:
                palindrome_str = line
                break
        if palindrome_str != '':
            break

    print(f'#{test_case + 1} {palindrome_str}')

"""
강사님이 짜주신 코드
for i in range(N // 2):
    if arr[i] != arr[N - 1 - i]:        # 회문이 아님!
        break
else:                                   # for문에서 break가 한번도 안 걸림!
    print("나 회문이야!")

# 행 검사하고 전치 행렬을 만들어서 그대로 넣어주면 열 검사도 가능하다!
"""