# SWEA 1210.[S/W 문제해결 기본] 2일차 - Ladder1
import sys
sys.stdin = open('sample_input/sample_input(11).txt', 'r')

for _ in range(10):
    test_case = int(input())

    matrix = []
    entrances = [-1]
    start_point = -1

    first = list(map(int, input().split()))
    matrix.append(first)

    for _ in range(first.count(1)):
        idx = first[entrances[-1] + 1:].index(1)
        entrances.append(entrances[-1] + idx + 1)

    entrances.pop(0)
    
    for i in range(1, 100):
        matrix.append(list(map(int, input().split())))

    for idx, e in enumerate(entrances):     
        road = [(0, 0)]
        x = 0
        y = entrances[idx]
        road.append((x, y))  

        while True:          
            if matrix[x][y] == 2:
                start_point = e
                break
            
            # 종료 조건
            if len(road) >=3 and road[-2] == road[-3] :
                break

            # 직진
            if x < 99 and matrix[x + 1][y] >= 1:
                if road[-2] != (x + 1, y):
                    x += 1
                    road.append((x, y))
            
            # 우회전
            if 0 <= y < 99 and matrix[x][y + 1] >= 1:
                if road[-2] != (x, y + 1):
                    y += 1
                    road.append((x, y))
                    continue
            
            # 좌회전
            if 0 < y <= 99 and matrix[x][y - 1] >= 1:
                if road[-2] != (x, y - 1):
                    y -= 1
                    road.append((x, y))
                    continue

            road.append((x, y))

        road.pop(0)

        if start_point != -1:   
            break

    print(f'#{test_case} {start_point}')
        