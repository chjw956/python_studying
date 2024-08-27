# SWEA 24.08.27.(화) - 1231. [S/W 문제해결 기본] 9일차 - 중위순회 (D4)
# 주어진 트리를 중위순회(inorder) 형식으로 순회하여 각 노드를 읽으면 특정 단어를 알 수 있다.
# 이렇게 트리를 순회하여 나오는 단어를 출력하라.
# 리스트 내에 객체들이 담겨있을 때, 그 리스트를 출력하면 해당 객체들의 내장__str__ 함수가 실행되지 않는다.
# 그냥 객체들이 담긴 리스트 그 자체가 출력됨


import sys
sys.stdin = open('sample_input\sample_input(41).txt', 'r')

from collections import deque

class TreeNode:
    def __init__(self, key):
        self.key = key  # 노드의 값
        self.left = None  # 왼쪽 자식 노드를 가리킴
        self.right = None  # 오른쪽 자식 노드를 가리킴
    def __str__(self) -> str:
        return str(self.key)
    
class BinaryTree:
    def __init__(self):
        self.root = None  # 트리의 루트 노드

    # 새로운 노드를 삽입하는 함수 (레벨 순서 삽입)
    def insert(self, key):
        new_node = TreeNode(key)
        if self.root is None:
            self.root = new_node
            return

        # 레벨 순서로 트리를 탐색하기 위해 큐를 사용
        queue = deque([self.root])

        while queue:
            node = queue.popleft()

            # 왼쪽 자식이 비어있으면 삽입
            if node.left is None:
                node.left = new_node
                break
            else:
                queue.append(node.left)

            # 오른쪽 자식이 비어있으면 삽입
            if node.right is None:
                node.right = new_node
                break
            else:
                queue.append(node.right)

    def inorder_traversal(self):
        # 중위 순회를 통해 트리의 노드들을 출력하는 함수
        result = self._inorder_traversal(self.root, [])
        return result

    # private 메서드
    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)
        str_result = ''
        for el in result:
            str_result += str(el)
        return str_result

T = 10

for tc in range(1, T + 1):
    # 트리가 갖는 정점의 총 수 N
    N = int(input())
    tree = BinaryTree()

    for _ in range(N):
        inputs = list(input().split())
        node = TreeNode(inputs[1])
        if len(inputs) > 2:
            node.left = inputs[2]
        
        if len(inputs) > 3:
            node.right = inputs[3]

        tree.insert(node)
    
    print(f'#{tc}', end = ' ')
    print(tree.inorder_traversal())