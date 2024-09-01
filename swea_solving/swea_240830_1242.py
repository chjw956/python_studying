# SWEA 24.08.30.(금) - 1242.[S/W 문제해결 응용] 1일차 - 암호코드 스캔(D5)
# 8개의 숫자로 이루어진 암호코드(고유번호 7개 + 검증코드 1개)
# 각 숫자 하나가 차지하는 최소 칸 수는 7칸(비트)이다.
# 암호코드 선의 두께가 굵어질 경우, 56의 배수의 길이를 가짐
# 암호코드 하나에 포함되는 암호코드 숫자들은 모두 동일한 크기를 가짐
# 암호코드 하나의 최대 길이는 448이다.
# 배열에는 비정상적인 암호코드가 포함될 수 있다.
# 정상 암호코드들에 적혀있는 숫자들의 합을 출력하라.
# 각 암호코드의 둘레에는 최소 1칸 이상의 빈 공간이 존재한다.
import sys
sys.stdin = open('sample_input\sample_input(48)_1.txt', 'r')


# 16진수를 십진수로(?) 변환
def hexaTodeci(s):
    hexadecimal = list("0123456789ABCDEF")
    return hexadecimal.index(s)


# 10진수를 2진수(문자열)로 표현
def deciTobi(n):
    result = []
    while n != 0:
        result.insert(0, n % 2)
        n //= 2
    
    return ''.join(str(i) for i in result)


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
T = 1

for tc in range(1, T + 1):
    # N: 배열의 세로 크기, M: 배열의 가로 크기
    N, M = map(int, input().split())

    # 16진수 값으로 이루어진 M개의 배열 값 입력받음
    matrix = list(input() for _ in range(N))

    whereNotZero = list([] * (M) for _ in range(N))
    
    result = 0

    print(f'#{tc}', end = ' ')

    # 0에서 값이 바뀌거나 다른 값에서 0으로 바뀌는 지점의 인덱스 값 저장
    for i in range(N):
        for j in range(0, M - 1):
            if (matrix[i][j] == '0') and (matrix[i][j] != matrix[i][j + 1]):
                whereNotZero[i].append(j + 1)
            elif (matrix[i][j] != '0') and (matrix[i][j + 1] == '0'):
                whereNotZero[i].append(j)
    
    # 암호코드 숫자가 존재하는 행의 정보
    sr = [i for i in range(len(whereNotZero)) if whereNotZero[i] != []]
    num = 0
    start = sr[num]

    while start < sr[-1] + 1:
        # 암호의 시작점에 해당하는 열의 인덱스 값 저장
        sc = [whereNotZero[start][j] for j in range(len(whereNotZero[start])) if j % 2 == 0]
    
        # si행에서 마지막 암호코드 숫자가 존재하는 위치
        ec = [whereNotZero[start][j] for j in range(len(whereNotZero[start])) if j % 2 != 0]

        sk = sc[num]
        ek = ec[num]

        # 16진수를 2진수로 표현한 문자열 생성
        password = ''
        for s in matrix[start][sk : ek + 1]:
            password += deciTobi(hexaTodeci(s))
        
        print(f'password = {password}, len(password) = {len(password)}')
        
        find = False                        # 암호를 찾았는지 체크
        change = False

        mul = len(password) // 56       # 현재의 길이가 몇 배인 건지

        # 현재의 길이가 56자보다 작은 경우 56자로 길이 설정
        if mul == 0:
            mul = 1
            
        target = mul * 56               # 목표로 하는 길이 설정
        toFill = target - len(password) # 목표 길이를 채우기 위해 필요한 공간의 수

        for k, v in passwords.items():
            for i in range(len(v)):
                v[i] *= mul

        password = '0' * toFill + password


        # 시작점 설정
        for k in range(sk - toFill, sk + 1):
            # 혹시 몰라서 넣은 조건인데, 필요없는지 마지막에 생각해보자.
            if k < 0:
                continue
            
            value = -1          # 해석한 숫자 저장 변수
            rslt = []
            # 시작점 기준 7 * mul 비트씩 잘라서 숫자 하나로 해석함
            # 8개의 숫자가 있다고 가정하고 보니까..
            for cnt in range(8):
                # print(f'{k + (7 * mul * cnt)} : {k + 7 * mul * (cnt + 1)}')
                value = interpreter(password[(k + (7 * mul * cnt)) : (k + 7 * mul * (cnt + 1))])
                if value == -1:
                    break
                rslt.append(value)

            # 만약 해석 불가능하다면 넘어감
            if value == -1:
                continue

            # 모아둔 배열을 해독한 결과값이 10의 배수이면
            if isThisMulTen(rslt):
                find = True
                result += sum(rslt)
                print(result)
                break
        
        for i in range(start + 1, len(whereNotZero)):
            if whereNotZero[i] != [] and whereNotZero[i] != whereNotZero[start]:
                num = i 
                change = True
        if not change:
            print(result)
            break