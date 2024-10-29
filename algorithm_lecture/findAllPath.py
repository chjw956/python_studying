def find_paths(N, x=0, y=0, path=None, result=None):
    if path is None:
        path = [(0, 0)]  # 시작점 [0, 0] 경로에 추가
    if result is None:
        result = []

    # 도착점에 도달하면 경로를 결과에 추가
    if x == N - 1 and y == N - 1:
        result.append(list(path))  # 깊은 복사로 경로 저장
        return

    # 오른쪽으로 이동 (경계 체크)
    if y + 1 < N:
        path.append((x, y + 1))
        find_paths(N, x, y + 1, path, result)
        path.pop()  # 백트래킹으로 상태 복원

    # 아래쪽으로 이동 (경계 체크)
    if x + 1 < N:
        path.append((x + 1, y))
        find_paths(N, x + 1, y, path, result)
        path.pop()  # 백트래킹으로 상태 복원

    return result

# 테스트
N = 3  # 3x3 지도 예시
all_paths = find_paths(N)

print("모든 경로:")
for path in all_paths:
    print(path)