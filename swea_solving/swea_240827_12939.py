# SWEA 24.08.27.(화) - 5176.[파이썬 S/W 문제해결 기본] 8일차 - 이진탐색(D2)
# 1부터 N까지의 자연수를 이진 탐색 트리에 저장하려고 한다.
# 중위 순회를 따른다고 할 때(?)
# N이 주어졌을 때 완전 이진 트리로 만든 이진 탐색 트리의 루트에 저장된 값과, 
# N/2번 노드(N이 홀수인 경우 소수점 버림)에 저장된 값을 출력하는 프로그램을 만드시오.

import sys
sys.stdin = open('sample_input\sample_input(39).txt', 'r')


def inorder(tree, idx, n):
    global num

    if idx > n:
        return
    
    inorder(tree, 2 * idx, n)
    tree[idx] = num
    num += 1
    inorder(tree, 2 * idx + 1, n)
    

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num = 1
    idx = 1
    tree = [0] * (N + 1)

    inorder(tree, idx, N)
    print(f'#{tc} {tree[1]} {tree[N//2]}')