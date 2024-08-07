# SWEA 2005.파스칼의 삼각형 (D2)
"""
스택 사용하기! -> 정훈이 코드 참고함!
stack1에서 꺼내서 출력하고 다음 줄에 출력할 값들을 stack2에 넣어두고
마지막에 stack2 값들을 stack1으로 그대로 옮겨주기!

로직은 생각했는데, 구현하는 데 어려움을 느끼는 상황에서 정훈이 코드 참고해서 구현 완료함!
"""

# (정석) 메모이제이션 사용하기

# T = int(input())

# stack 2개, append(), pop() 사용 버전

# for test_case in range(T):
#     N = int(input())

#     stack1, stack2 = [], []

#     stack1.append(1)

#     print(f'#{test_case + 1}')

#     # i = 0, 1, 2, 3
#     for i in range(N):
#         print(' '.join(map(str, stack1)))
#         stack2.append(stack1[-1])
        
#         # i = 1, 2, 3
#         for j in range(i):
#             stack2.append(stack1.pop() + stack1[-1])
        
#         # 마지막 항은 무조건 1
#         stack2.append(1)

#         stack1, stack2 = stack2, []



# stack 2개, top 사용 버전

# for test_case in range(T):
#     N = int(input())

#     stack1, stack2 = [''] * N, [''] * N
#     top1, top2 = -1, -1

#     top1 += 1
#     stack1[top1] = '1'

#     print(f'#{test_case + 1}')

#     for i in range(N-1):
#         print(' '.join(stack1))

#         top2 += 1
#         stack2[top2] = stack1[top1]
        
#         for j in range(i):
#             # stack1.pop()
#             v = int(stack1[top1])
#             top1 -= 1

#             # + stack1[-1]
#             v += int(stack1[top1])

#             top2 += 1
#             stack2[top2] = str(v)
        
#         # 마지막 항은 무조건 1
#         top2 += 1
#         stack2[top2] = '1'

#         stack1, stack2 = stack2, [''] * N
#         top1, top2 = top2, -1

#     print(' '.join(stack1))



# 강사님 버전(재귀 함수)
# 재귀 함수를 생성할 때에는 전체 로직보다는 함수 하나의 로직을 생각하면 됨!
# 재귀 함수 호출의 최대 횟수는 1000번이다.


# 파스칼 삼각형의 row행을 그리는 함수
def recursion(arr, row, n):
    if row == n:
        return
    
    # row + 1개의 열에 숫자 채우기
    for r in range(row + 1):
        if r == 0:
            arr[r][0] = 1
            continue

        for j in range(r + 1):
            # 첫 열은 항상 1
            if j == 0:
                arr[r][j] = 1
            
            # 이후의 j번째 열
            else:
                arr[r][j] = arr[r-1][j] + arr[r-1][j-1]
    recursion(arr, row + 1, n)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    recursion(arr, 0, N)

    print(f'#{tc}')
    for i in range(N):
        for j in range(i + 1):
            print(arr[i][j], end=" ")
        print()