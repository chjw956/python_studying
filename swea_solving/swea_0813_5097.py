# SWEA 5097.[파이썬 S/W 문제해결 기본] 6일차 - 회전 (D2)

import sys
sys.stdin = open('sample_input(25).txt', 'r')

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


    def __str__(self):
        return str(self.value)


class MyQueue:
    def __init__(self):
        self.front = None
        self.rear = None
    

    def enQueue(self, item):
        new_node = Node(item)

        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    
    def deQueue(self):
        prev = self.front
        self.front = prev.next
        return prev


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    values = list(map(int, input().split()))

    my_queue = MyQueue()

    for n in range(N):
        my_queue.enQueue(values[n])

    for m in range(M):
        prev = my_queue.deQueue()
        my_queue.enQueue(prev.value)

    print(f'#{tc} {my_queue.deQueue().value}')