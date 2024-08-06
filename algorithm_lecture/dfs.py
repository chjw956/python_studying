# 24.08.06.(화) [DFS] 다음은 연결되어 있는 두 정점 사이의 간선을 순서대로 나열해둔 것이다. 
# 모든 정점을 깊이 우선 탐색(DFS)하여 화면에 경로를 출력하시오. (시작 정점은 1로 한다.)

"""
출력 결과
1 2 4 6 5 7 3
"""


def dfs(graph):
    global top
    global my_stk
    global visited
    
    top += 1
    my_stk.append(graph.keys()[0])
    visited.append(graph.keys()[0])

    # 로직을 어떻게 짜야 하지?
    while True:
        top += 1
        my_stk.append(i for i in graph[my_stk[top-1]])

        if 
        




information = list(map(int, input().split()))           # 1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7 입력
my_graph = dict()

# 입력된 값을 이용해 무방향 그래프 생성
for i in range(0, len(information), 2):
    if information[information[i]] in my_graph:
        my_graph[information[i]].append(information[i+1])
    else:
        my_graph[information[i]] = [information[i + 1]]

    if information[i + 1] in my_graph:
        my_graph[information[i + 1]].append(information[i])
    else:
        my_graph[information[i + 1]] = [information[i]]

my_stk = []             # 스택
top = -1
visited = []               # 방문한 정점


