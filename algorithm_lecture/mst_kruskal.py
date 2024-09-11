# V: 마지막 정점. 따라서 정점의 개수는 (V+1)개이다.
# E: 간선의 개수
V, E = map(int, input().split())    
edge = []

# 간선 집합 생성
for _ in range(E):
    u, v, w = map(int, input().split())
    edge.append([u, v, w])
edge.sort(key=lambda x : x[2])          # 가중치 기준 오름차순 정렬
parents = [i for i in range(V)]         # 대표원소 배열


def find_set(x):
    if parents[x] == x:
        return x

    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    x = find_set(x)
    y = find_set(y)

    if x == y:
        return

    # 더 작은 루트노트에 합침
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


# MST의 간선수 N = 정점 수 - 1
cnt = 0     # 선택한 edge의 수
total = 0   # MST 가중치의 합
for u, v, w in edge:
    # 다른 집합이라면
    if find_set(u) != find_set(v):
        cnt += 1
        union(u, v)
        total += w
        if cnt == V:  # MST 구성이 끝나면
            break
print(f'최소 비용 = {total}')


'''
# 입력
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 4 46
2 6 25
3 4 34
3 5 18
4 5 40
4 6 51
'''