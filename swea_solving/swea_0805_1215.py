# SWEA 1215. [S/W 문제해결 기본] 3일차 - 회문1 (D3)
# 회문(Palindrome)

def isPalindrome(arr, st_pt, cpr_pt):
    for _ in range(st_pt, -1, -1):
        if arr[st_pt] == arr[cpr_pt]:
            st_pt -= 1
            cpr_pt += 1
        else:
            return False
    return True

import sys
sys.stdin = open('sample_input\sample_input(17).txt', 'r')

for _ in range(10):
    L = int(input())            # 회문의 길이
    N = 8                       # 글자판의 크기

    matrix = []
    for __ in range(N):
        matrix.append(list(input()))

    cnt = 0                     # 찾은 회문의 개수

    if L > 1:
        # L > 1
        # 행 기준
        for r in matrix:
            for idx, c in enumerate(r[:N - L + 1]):             # 문자열 시작점
                # 회문의 길이가 짝수라면,
                if L % 2 == 0:
                    result = isPalindrome(r[idx:idx + L], L//2 - 1, L//2)
                # 회문의 길이가 홀수라면,
                else:
                    result = isPalindrome(r[idx:idx + L], (L - 1) // 2 - 1, (L - 1) // 2 + 1)
                if result == True:
                    cnt += 1

        # 열 기준
        for j in range(N):
            arr = []
            for i in range(N):                              # 문자열 시작점
                arr.append(matrix[i][j])

            for i in range(N - L + 1):
                if L % 2 == 0:
                    result = isPalindrome(arr[i:i + L], L//2 - 1, L//2)
                else:
                    result = isPalindrome(arr[i:i + L], (L - 1) // 2 - 1, (L - 1) // 2 + 1)
            
                if result == True:
                    cnt += 1
    # L == 1
    else:
        cnt = N ** 2


    print(f'#{_ + 1} {cnt}')


