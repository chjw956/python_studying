# 백준 11651. 좌표 정렬하기2 (Silver 2)

N = int(input())

coordinates = []

for _ in range(N):
    x, y = map(int, input().split())
    coordinates.append((x, y))

coordinates.sort(key=lambda x:(x[1], x[0]))            # 좌표를 y가 증가하는 순으로 정렬

for (x, y) in coordinates:
    print(f'{x} {y}')