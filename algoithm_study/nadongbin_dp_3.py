# 3. 개미 전사
# 식량 창고 N개가 주어질 때, 개미 전사들은 식량창고를 선택적으로 약탈하여 최대한 많은 식량을 가져오고자 한다.
# 단 메뚜기 정찰병들이 일직선상에 존재하는 식량 창고 중에 서로 인접한 식량창고가 습격받은 사실을 눈치챌 수 있다고 할 때,
# 개미 전사들은 정찰병에게 들키지 않고 약탈해야 한다.

N = int(input())
grocery = list(map(int, input().split()))

# 앞서 계산된 결과 저장을 위한 DP 테이블 초기화
d = [0] * 100

# DP 진행 (Bottom-Up)
d[0] = grocery[0]
d[1] = max(grocery[0], grocery[1])

for i in range(2, N):
    d[i] = max(d[i - 1], d[i - 2] + grocery[i])

print(d[N - 1])