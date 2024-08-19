"""
Im_ 로 파일명 표기시, Im에 응시한 것으로 간주함
Im_ 를 제외한 파일명의 경우
"""
# 조명 제어
# i 번째 버튼을 누르면 i의 배수에 해당하는 LED의 상태가 변경됨
# LED가 모두 꺼져있는 상태에서 원하는 패턴으로 만들기 위해 스위치 조작을 하려고 함
# 원하는 패턴이 주어질 때 이를 만들기 위한 최소 스위치 조작 횟수?


def reverse_led(lst, n):
    for i in range(len(lst)):
        if (i + 1) % n == 0:
            if lst[i] == 0:
                lst[i] = 1
            else:
                lst[i] = 0
    return lst


def isTheseSame(lst1, lst2):
    for _ in range(len(lst1)):
        if lst1[_] != lst2[_]:
            return False

    return True


T = int(input())

for tc in range(1, T + 1):
    N = int(input())             # N: LED 등 및 버튼의 수
    led_pattern = list(map(int, input().split()))               # 0은 OFF, 1은 ON 상태를 말함

    # 초기 led 상태
    led_now = [0] * N

    # 현재의 led와 원하는 led 패턴에서 일치하지 않는 인덱스 값 목록
    idxs = []
    cnt = 0

    while not isTheseSame(led_now, led_pattern):
        cnt += 1
        for i in range(N):
            if led_pattern[i] != led_now[i]:
                idxs.append(i)

        reverse_led(led_now, idxs[0] + 1)
        idxs = []

    print(f'#{tc} {cnt}')
