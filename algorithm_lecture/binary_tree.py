# 전위 순회 뼈대 코드
def preorder_traverse(T):
    if T:
        visit(T)            # print(T.item)
        preorder_traverse(T.left)
        preorder_traverse(T.right)


# 중위 순회 뼈대 코드
def inorder_traverse(T):
    if T:
        inorder_traverse(T.left)
        visit(T)            # print(T.item)
        inorder_traverse(T.right)


# 후위 순회 뼈대 코드
def postorder_traverse(T):
    if T:
        postorder_traverse(T.left)
        postorder_traverse(T.right)
        visit(T)            # print(T.item)


# 연습문제 3번 (트리) 답안 코드
# left, right를 쓰는 버전
# 단, 입력이 반드시 각 노드당 최대 2번씩만 들어온다고 가정한 코드임
"""
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""

# 전위 순회
# 그래프에서는 재귀 호출을 반드시 사용하게 되어 있음
# 실제 개발에서는 class 내부에 left, right 멤버 변수를 이용해 연결리스트로 많이 표현함
def preorder(node):
    if node == 0:
        return
    
    # 내 차례
    print(node, end = ' ')
    # 왼쪽 자식 차례
    preorder(left[node])
    # 오른쪽 자식 차례
    preorder(right[node])


# 중위 순회
def inorder(node):
    if node == 0: 
        return
    # 왼쪽 자식 차례
    inorder(left[node])
    # 내 차례
    print(node, end=' ')
    # 오른쪽 자식 차례
    inorder(right[node])


# 후위 순회
def postorder(node):
    if node == 0:
        return
    # 왼쪽 자식 차례
    postorder(left[node])
    # 오른쪽 자식 차례
    postorder(right[node])
    # 내 차례
    print(node, end = ' ')
    

N = int(input())
E = N - 1
arr = list(map(int, input().split()))

# 왼쪽 자식 번호를 저장할 리스트
left = [0] * (N + 1)

# 오른쪽 자식 번호를 저장할 리스트
right = [0] * (N + 1)

# 자식을 인덱스로 하여 부모 저장
par = [0] * (N + 1)

for i in range(E):
    parent, child = arr[i * 2], arr[i * 2 + 1]

    # 왼쪽 자식이 없다면, 왼쪽에 삽입함
    if left[parent] == 0:
        left[parent] = child
    # 왼쪽 자식은 있지만, 오른쪽 자식이 없다면 오른쪽에 삽입함
    else:
        right[parent] = child
    par[child] = parent

c = N

while par[c] != 0:          # 부모가 있으면
    c = par[c]              # 부모를 새로운 자식으로 두고

# 더이상 부모가 없다면, root
root = c

print(f'par = {par}')
print(f'left = {left}')
print(f'right = {right}')

# 전위 순회
preorder(root)
print()
# 중위 순회
inorder(root)
print()
# 후위 순회
postorder(root)