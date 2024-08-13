# SWEA 24.08.13.(화) 12719.[파이썬 S/W 문제해결 기본] 6일차 - 피자 굽기 (D3)
# 원형 큐 -> 클래스로 구현?

import sys
sys.stdin = open('sample_input(26)_1.txt', 'r')


def enQueue(item):
    global rounded_queue
    global rear
    global out

    if isFull():
        print("Queue is Full now!")
    else:
        rear = (rear + 1) % N
        rounded_queue[rear] = item


def deQueue():
    global rounded_queue
    global front
    global rear

    if isEmpty():
        print("Queue is Empty now!")
    else:     
        front = (front + 1) % N
        return rounded_queue[front]


def isFull():
    global rounded_queue
    global rear

    print(f'isFull(front = {front}, rear = {rear})')
    return (rear + 1) % N == front


def isEmpty():
    return front == rear
    

T = int(input())

for tc in range(1, T + 1):
    # N: 화덕의 크기, M: 피자의 개수
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    
    prev = M - N - 1
    out = 0

    for (i, l) in enumerate(lst):
        lst[i] = [i, l]
    
    lst.reverse()

    rounded_queue = [None] * N
    front = -1
    rear = -1
    ctn = True

    for n in range(N):
        enQueue(lst.pop())
    
    print(f'queue = {rounded_queue}')
    