"""
# (선형) Queue를 이용하여 마이쮸 나눠주기 시뮬레이션을 해보자.
- 엔터(Enter)를 칠 때마다 아래의 정보를 화면에 출력
    1. 큐에 있는 사람의 수
    2. 현재 일인당 나눠주는 사탕의 수
    3. 현재까지 나눠준 사탕의 수

"""
import time


def isFull():
    global queue
    global rear

    if rear == len(queue) -1 :
        return True
    
    return False


def enQueue(item):
    global queue
    global rear

    if isFull():
        print("Queue is Full now!")
    else:
        rear += 1
        queue[rear] = item


def deQueue():
    global queue
    global front
    global rear
    
    if front == rear:
        print("Queue is Empty now!")
    else:
        front += 1
        return queue[front]


def pressEnter():
    global front
    global rear
    global queue
    global myChew

    input("엔터를 입력해주세요.")

    who = None
    
    for i in range(front + 1, rear + 1):
        who = queue[i][0]
        myChew -= queue[i][1] 
        deQueue()

        print(f'큐에 있는 사람의 수: {rear - front}')
        print(f'현재 일인당 나눠주는 사탕의 수: {queue[i][1]}')
        print(f'현재까지 나눠준 사탕의 수:  {20 - myChew}')
        print()
    
    print('**************************************')
    print()
    time.sleep(0.1)
    return who
    

myChew = 20
front = rear = 0
queue = [None] * 1000000

cnt = 1

while myChew != 0:
    k = 1
    n = cnt + 1

    for i in range(cnt):
        enQueue((k, n - k))
        k += 1
    
    who = pressEnter()

    front = rear
    cnt += 1

print(f'사탕을 마지막으로 가져간 사람: {who}')