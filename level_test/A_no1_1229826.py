# A형 검정 시험
# 하강 모의실험 (블록들을 동시에 하강시킨 후, 이 결과로부터 맨 왼쪽열에 있는 블록들을 동시에 우측 하강시킨 결과를 알아내시오.)
# 출력할 값은, '맨 아래 행에 자리한 블록의 수와 맨 오른쪽 열에 자리한 블록의 수'를 차례로 나열할 것!

# 가장 상단에 있는 블럭들만 하강시키면 되는 듯!
# 동일한 열에 존재하는 것에 대해서만 덩어리를 이룰 수 있으며, 한 칸에 대해 처음 하강할 시 힘의 크기는 1이다.
# 한 칸 하강할 때마다 해당 블록의 하강 힘은 1.9배가 된다.
# 처음 하강은 아래로 진행되지만, 모든 블럭이 하강하고난 후에는 우측 하강이 이루어진다. (행 기준으로 변경됨)

import sys
sys.stdin = open('sample_input.txt', 'r')


def push_block(start, col_num, row_num, end, matrix, col = False, row = False):
    cnt_zero = 0                        # 밀어내지 않고 하강하면서 1.9를 곱할 칸의 수
    to_push = 0                         # 하강하면서 밀어야 할 블럭의 크기 측정
    # 아래로 블럭을 하강시킴
    if col == True:
        while start < end:
            if matrix[start][col_num] == 0:
                cnt_zero += 1
                start += 1
            else:
                to_push += 1
                if start < N - 1 and matrix[start + 1][col_num] == 0:
                    break
                start += 1
    # 우측으로 블럭을 하강시킴
    elif row == True:
        while start < end:
            if matrix[row_num][start] == 0:
                cnt_zero += 1
                start += 1
            else:
                to_push += 1
                if start < N - 1 and matrix[row_num][start + 1] == 0:
                    break
                start += 1

    return cnt_zero, to_push


for tc in range(1):
    if tc <= 2:
        # 아래쪽으로 하강만 함
        pass
    elif 2 < tc < 5:
        # 아래쪽 하강 후 우측 하강 블럭은 1개만 함
        pass
    else:
        # 아래쪽 하강 후 우측 하강 모두
        pass

    N = int(input())
    value = 1.9             # 한 칸씩 이동할 때마다 곱해질 힘의 값
    
    matrix = []

    # 입력된 값 기반, matrix 생성
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
.
0

    row_blocks = 0                  # 가장 아래 행의 블럭 수 카운팅
    col_blocks = 0                  # 가장 아래 열의 블럭 수 카운팅

    for (j, b) in enumerate(matrix[0]):
        if b != 0:
            power = b
            idx = b
            cnt_zero = -1

            while b < N:
                cnt_zero, to_push = push_block(b, j, N, matrix)
                
                if power * (value ** cnt_zero) <= to_push:
                    break
                else:
                    power *= value ** cnt_zero
                    power += to_push
                    b += cnt_zero + to_push
                    continue

            if b >= N:
                row_blocks += 1

    push_col = []


    # for (j, b) in enumerate(matrix[0]):
    #     if b != 0:
    #         power = b
    #         idx = b
    #         cnt_zero = -1
    #
    #         while b < N:
    #             cnt_zero, to_push = push_block(b, j, N, matrix)
    #
    #             if power * (value ** cnt_zero) <= to_push:
    #                 break
    #             else:
    #                 power *= value ** cnt_zero
    #                 power += to_push
    #                 b += cnt_zero + to_push
    #                 continue
    #
    #         if b >= N:
    #             row_blocks += 1

    print(f'#{tc} {row_blocks} {col_blocks}')