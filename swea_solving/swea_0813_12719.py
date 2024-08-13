# SWEA 24.08.13.(화) 12719.[파이썬 S/W 문제해결 기본] 6일차 - 피자 굽기 (D3)
# 원형 큐 -> 클래스로 구현?

import sys
sys.stdin = open('sample_input(26).txt', 'r')


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

    for m in range(M):
        front = -1
        rear = N - 1
        for n in range(N):
            if rounded_queue[n] != None:
                rounded_queue[n][1] //= 2

        for n in range(N):
            temp = deQueue()
            rounded_queue[front] = None

            if temp == None:
                continue

            if temp[1] == 0 :                       # 만약 치즈가 다 녹으면
                out += 1                            # 빼낸 개수 + 1
                if prev >= 0:                       # 만약 아직 대기중인 피자가 있다면
                    temp = lst[prev]                # 집어넣을 피자를 그것으로 설정
                    prev -= 1   
                elif out == M:                      # 빼낸 개수가 총 피자 개수와 같다면
                    # 마지막 피자 번호
                    print(f'# {tc} {temp[0] + 1}')
                    ctn = False                     # 최종 탈출
                # 만약 대기중인 피자가 없고, 빼낸 개수가 총 개수와 같지 않다면
                else:
                    continue
            
            rounded_queue[front] = temp 

        if ctn == False:
            break