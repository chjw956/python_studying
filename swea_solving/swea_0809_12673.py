# SWEA 24.08.09.(금) - 12673. [파이썬 S/W 문제해결 기본] 5일차 토너먼트 카드게임 (D2)
# 만약 같은 카드인 경우 편의상 번호가 작은 쪽(순서가 빠른 쪽)을 승자라고 한다.
# 토너먼트 구현

import sys
sys.stdin = open('sample_input\sample_input(34).txt', 'r')

# 왜 자꾸 테스트케이스 일부만 맞는 건지 모르겠음..

# 재귀로 구현
def winnerWho(lst, end):
    my_stack = []
    n = len(lst)

    # 인원이 1명인 경우
    if n == 1:
        my_stack.append(lst.pop())
        return my_stack

    # 인원이 2명인 경우
    if n == 2:
        # 만약 같은 카드인 경우 번호가 작은 쪽이 승자가 됨
        if lst[0][1] == lst[1][1]:
            lst.sort(key=lambda x:x[0])
            my_stack.append(lst[0])
            return my_stack
        
        lst.sort(key=lambda x:x[1])
        big = lst[1][1]
        small = lst[0][1]

        rslt = big / small

        if rslt <= 2:
            my_stack.append(lst[1])
        else:
            my_stack.append(lst[0])
        
        return my_stack
    
    # 인원이 3명 이상인 경우
    elif n >= 3:
        lst1 = winnerWho(lst[:n // 2 + 1], n // 2 + 1)
        lst2 = winnerWho(lst[n // 2 + 1 : end], end - n // 2 - 1)

        while lst1 :
            my_stack.append(lst1.pop())
        
        while lst2:
            my_stack.append(lst2.pop())

    return my_stack


T = int(input())

for tc in range(1, T + 1):
    N = int(input())            # 인원 수 N
    # 1은 가위, 2는 바위, 3은 보
    cards = list(enumerate(list(map(int, input().split()))))   # 카드의 인덱스값과 데이터를 튜플로 변환하여 저장      

    n = N
    
    while len(cards) > 1:
        cards = winnerWho(cards, n)
        n = len(cards)
        
    print(f'#{tc} {cards[0][0] + 1}')



"""
# 강사님 코드
# 홀수인 경우 좌측 그룹의 인원을 더 많이 포함시킴
def solve(i, j):
        if i == j:
            return i

        winner1 = solve(i, (i + j) // 2)
        winner2 = solve((i + j) // 2 + 1, j)

        print(f'winner1 = {winner1}, winner2 = {winner2}')

        result = winner1
        
        # 승자 두 명 뽑았으니 가위바위보 결과 계산하기
        if data[winner1] == 1 and data[winner2] == 2:
            result = winner2
        elif data[winner1] == 2 and data[winner2] == 3:
            result = winner2
        elif data[winner1] == 3 and data[winner2] == 1:
            result = winner2

        return result


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))

    print(f'#{tc} {solve(0, N - 1) + 1}')
    # 이 함수는 인덱스로 번호를 받았기 때문에
    # 실제 번호는 solve함수에 1을 더해주어야 함

"""
