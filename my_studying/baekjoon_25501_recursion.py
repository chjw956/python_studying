"""
# 함수 이용 코드

# 재귀 함수
def recursion(s, l, r):
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l+1, r-1)


def isPalindrome(s):
    return recursion(s, 0, len(s) - 1)


for test_case in range(T):
    string = input()

    print(isPalindrome(string))
"""

"""
# 처음 내가 짠 코드

cnt = 0
T = int(input())

for test_case in range(T):
    string = input()
    
    str_len = len(string)

    # 짝수 개의 문자로 이루어진 경우
    if str_len % 2 == 0:
        for n in range(str_len // 2):
            if string[n] != string[str_len - n - 1]:
                print(test_case + 1, 0)
                break
    
    # 홀수 개의 문자로 이루어진 경우
    if str_len % 2 != 0:
        for n in range((str_len - 1) // 2):
            if string[n] != string[str_len - n - 1]:
                print(test_case + 1, 0)
                break

    print(test_case + 1, 1)

"""

# 로직 파악 후 다시 짜본 코드
# 전역 변수로 저장해둬야 하나 싶은 숫자는 매개변수로 전달해주는 방식으로 구현하기!
def recursion(string, start, last):
    if start >= last:
        return 1, start+1
        # return 1
    if string[start] != string[last]:
        return 0, start+1
        # return 0
    else:
        return recursion(string, start + 1, last - 1)


def isPalindrome(string):
    return recursion(string, 0, len(string)-1)


T = int(input())

for test_case in range(T):
    string = input()
    result, num = isPalindrome(string)
    print(result, num)
