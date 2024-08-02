# SWEA 1210.[S/W 문제해결 기본] 2일차 - Ladder1
import sys
sys.stdin = open('sample_input/sample_input(11)_1.txt', 'r')

for _ in range(1):
    test_case = int(input())

    # 좌회전, 직진, 우회전
    di = [0, 1, 0]
    dj = [-1, 0, 1]
    d = list(zip(di, dj))

    matrix = []
    entrances = [-1]
    success = False
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
            
            find_root = []

            if x == 99 or y == 99:
                for forward in d:
                    if x + forward[0] <= 99 and y + forward[1] <= 99:
                        if road[-2] == (x + forward[0], y + forward[1]):
                            break

        road.pop(0)

        if start_point != -1:   
            break
        if e == 91:
            print(road)
    print(f'#{test_case} {start_point}')
        
"""
더이상 갈 곳이 없으면 멈추게 해야 함
"""