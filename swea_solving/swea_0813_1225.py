# SWEA 24.08.13.(화) - 1225. [S/W 문제해결 기본] 7일차 - 암호생성기 (D3)

import sys
sys.stdin = open('sample_input\sample_input(27).txt', 'r')

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
        
        if self.front == None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
    

    def deQueue(self):
        prev = self.front
        self.front = prev.next
        return prev


for _ in range(1, 11):
    tc = int(input())
    lst = list(map(int, input().split()))
    N = 8

    my_queue = MyQueue()
    for l in lst:
        my_queue.enQueue(l)
    
    cnt = 1
    node = my_queue.deQueue() 
    num = node.value

    while True:
        num -= cnt
        if num <= 0 :
            num = 0
            my_queue.enQueue(num)
            break
        my_queue.enQueue(num)
        if cnt == 5:
            cnt = 1
        else:
            cnt += 1
        node = my_queue.deQueue() 
        num = node.value

    print(f'#{tc}', end = ' ')
    for _ in range(N):
        print(my_queue.deQueue().value, end = ' ')
    print()