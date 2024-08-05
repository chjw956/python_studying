# SWEA 12592. 4865.[파이썬 S/W 문제해결 기본] 3일차 - 글자수 (D2)

"""
문자열 str1에 포함된 글자들이 str2에 몇 개씩 들어있는지 찾고, 
그중 가장 많은 글자의 개수를 출력하라.
"""
import sys
sys.stdin = open('sample_input\sample_input(15).txt', 'r')

T = int(input())

for test_case in range(T):
    str1 = input()
    str2 = input()

    N = len(str1)
    M = len(str2)
    
    string = []
    how_many = []

    for i in range(N):
        string.append(str1[i])
        count = 0
        for j in range(M):
            if str2[j] == str1[i]:
                count += 1
        how_many.append(count)
    
    numbers = list(zip(string, how_many))
    numbers.sort(key = lambda x:x[1], reverse=True)
    print(f'#{test_case + 1} {numbers[0][1]}')