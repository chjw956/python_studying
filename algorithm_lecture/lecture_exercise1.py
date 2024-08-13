"""
# 선형 큐
큐를 구현하여 아래 동작을 확인해보자.
세 개의 데이터 1, 2, 3을 차례로 큐에 삽입하고 큐에서 세 개의 데이터를 차례로 꺼내어 출력
(1, 2, 3이 출력되어야 함)

"""

def enQueue(item):
    global queue
    global rear

    if isFull():
        print("Queue is Full now!")
    else:
        rear += 1
        queue[rear] = item


def isFull():
    global queue
    global rear

    if rear == len(queue) -1 :
        return True
    
    return False


def deQueue():
    global queue
    global front
    global rear
    
    if front == rear:
        print("Queue is Empty now!")
    else:
        front += 1
        return queue[front]
    

queue = [None] * 1000000
front = rear = 0

enQueue(1)
enQueue(2)
enQueue(3)

print(deQueue(), end = ' ')
print(deQueue(), end = ' ')
print(deQueue(), end = ' ')