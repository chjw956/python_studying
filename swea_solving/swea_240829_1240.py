# SWEA 24.08.29.(목) - 1240. [S/W 문제해결 응용] 1일차 - 단순 2진 암호코드 (D3)
# 암호코드는 8개의 숫자로 이루어지며 암호코드에서의 숫자 하나는 7개의 비트로 암호화되어 주어짐 -> 따라서 총 가로 길이는 56이다.
# 암호코드는 (홀수 자리의 합) x 3 + (짝수 자리의 합) % 10 = 0이다.
# 암호코드 정보가 포함된 2차원 배열을 입력받아 올바른 암호코드인지 판별하는 프로그램을 작성하라.
# 암호코드 이외의 부분은 전부 0으로 주어진다.
# 주어진 암호코드가 올바른 암호코드인 경우 암호코드에 포함된 숫자의 합을 출력하고, 잘못된 암호코드인 경우 0을 출력하라.

import sys
sys.stdin = open('sample_input\sample_input(47).txt', 'r')

# 7비트의 암호를 하나의 숫자로 해석
def interpreter(string):
    comb = []
    cnt = 1
    before = string[0]

    # 이전의 숫자와 같지 않으면 지금까지 카운팅한 수를 comb 리스트에 추가하고 
    # cnt를 1로 초기화함
    for s in string[1:]:
        if before != s:
            comb.append(cnt)
            cnt = 1
            before = s
        else:
            cnt += 1
            before = s
    comb.append(cnt)
    
    # comb 리스트에 존재하는 수가 4개가 넘어가면 -1 반환
    if len(comb) > 4:
        return -1
    
    # passwords 딕셔너리에서 comb 배열과 동일한 value를 갖는 key 값을 찾음
    value = [k for k, v in passwords.items() if v == comb]

    # 만약 동일한 배열을 갖는 key 값이 없다면 -1 반환
    if not value:
        return -1

    return value[0]


# 해독한 값이 10의 배수가 되는지 확인
def isThisMulTen(lst):
    even = 0            # 짝수 자리의 합
    odd = 0             # 홀수 자리의 합
    rslt = 0            # 해독한 결과 값
    for idx in range(8):
        # 홀수 자리이면
        if idx % 2 == 0:
            odd += lst[idx]
        # 짝수 자리이면
        else:
            even += lst[idx]

    rslt = odd * 3 + even

    # 해독한 결과값이 10의 배수인지 아닌지
    if rslt % 10 == 0:
        return True
    else:
        return False


passwords = {0: [3, 2, 1, 1],
             1: [2, 2, 2, 1],
             2: [2, 1, 2, 2],
             3: [1, 4, 1, 1],
             4: [1, 1, 3, 2], 
             5: [1, 2, 3, 1], 
             6: [1, 1, 1, 4],
             7: [1, 3, 1, 2], 
             8: [1, 2, 1, 3], 
             9: [3, 1, 1, 2]}

T = int(input())

for tc in range(1, T + 1):
    # N: 배열의 세로 크기, M: 배열의 가로 크기
    N, M = map(int, input().split())

    # 암호코드 정보가 포함된 2차원 배열을 입력받음
    matrix = list(input() for _ in range(N))
    used = [False for _ in range(56)]

    # 암호를 찾았는지 체크
    find = False
    print(f'#{tc}', end = ' ')
    
    # 첫 번째 1이 존재하는 위치
    si, sk = 0, 0

    for i in range(N):
        for k in range(M):
            if matrix[i][k] == '1':
                si, sk = i, k
                break
        if si or sk:
            break

    # si행에서 마지막 1이 존재하는 위치
    ek = 0
    for idx in range(M-1, -1, -1):
        if matrix[si][idx] == '1':
            ek = idx
            break
    
    # 현재 발견한 암호의 길이
    length = ek - sk + 1

    # 채워야 하는 암호의 길이
    toFill = 56 - length

    # 시작점을 어디로 할지를 찾기
    for idx in range((sk - toFill), sk + 1):
        value = -1          # 해석한 숫자를 저장할 변수
        rslt = []           # 해석한 숫자들을 모아둘 배열
        # 시작점 기준 7비트씩 잘라서 숫자 하나로 해석
        for cnt in range(8):
            value = interpreter(matrix[si][idx + (7 * cnt) : idx + 7 * (cnt + 1)])
            if value == -1:
                break
            rslt.append(value)

        # 만약 해석 불가능하다면 넘어감
        if value == -1:
            continue
        
        # 모아둔 배열을 해독한 결과값이 10의 배수이면
        if isThisMulTen(rslt):
            find = True
            print(sum(rslt))
            break
    
    # 암호코드가 올바르지 않은 경우 0 출력
    if not find:
        print(0)