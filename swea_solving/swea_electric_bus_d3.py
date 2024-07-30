import sys
sys.stdin = open('sample_input(3).txt', 'r')

T = int(input())

for test_case in range(T):
    # K : 한번 충전으로 최대 이동 정류장 수
    # N : 종점 정류장
    # M : 충전기가 설치된 정류장 개수
    # 출발지에는 항상 충전기가 설치되어 있지만 충전 횟수에는 포함하지 않음
    K, N, M  = map(int, input().split())
    charge_spot = list(map(int, input().split()))
    differences = [charge_spot[0]]
    keep = True
    cnt = 0                 # 멈춰야 하는 횟수 카운팅
    sum_value = 0
    start_idx = 0

    # K부터 충전해야 하는 거니까 K - M 사이에 몇 번 충전해야 하는지를 반환하면 됨
    for idx in range(len(charge_spot)-1):
        difference = charge_spot[idx + 1] - charge_spot[idx]
        differences.append(difference)
     
    differences.append(N - charge_spot[-1])
    
    for difference in differences:
        if difference > K:
            keep = False
    
    if keep == False:
        print(f'#{test_case + 1} {cnt}')
        continue
        
    # 처음 충전한 것으로 K만큼 이동하고 시작할 수 있는 경우
    if K in charge_spot:
        cnt += 1
        start_idx = charge_spot.index(K) + 1

    for idx in range(start_idx, len(differences)):
        sum_value += differences[idx]
        if sum_value > K :
            sum_value = differences[idx]
            cnt += 1

    print(f'#{test_case + 1} {cnt}')
