# SWEA 24.09.09.(월) 12741. 두 전구 (D4)
# 두 전구 X, Y에 대해 0초부터 100초간 두 전구가 언제 켜지는지 관찰했을 때,
# 두 전구가 동시에 켜져 있던 시간은 몇 초인가?

# 답안 (라이브 강사님 코드)
import sys
sys.stdin = open('sample_input\sample_input(62).txt', 'r')

T = int(input())
result_lst = []

for tc in range(1, T + 1):
    # A: X 전구가 켜지는 시각, B: X 전구가 꺼지는 시각
    # C: Y 전구가 켜지는 시각, D: Y 전구가 꺼지는 시각
    A, B, C, D = map(int, input().split())

    # 나중에 켜진 전구 시각이 시작점
    start_time = max(A, C)
    
    # 먼저 꺼진 전구 시각이 종료점
    end_time = min(B, D)

    result = end_time - start_time

    if result <= 0:
        result = 0
    
    result_lst.append(result)

for index, result in enumerate(result_lst):
    print(f'#{index + 1} {result}')