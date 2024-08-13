# 요소의 정보를 저장하기 위한 클래스
class Node:
    # 데이터를 저장할 변수
    # 다음 요소를 가리키기 위한 변수
    def __init__(self, value):
        self.value = value
        self.next = None
    

    def __str__(self):
        return str(self.value)


class MyQueue:
    # 상태값 front와 rear를 가짐
    # enQueue(), deQueue(), Qpeek()을 멤버 메서드로 가짐
    # Qpeek()은 요소를 삭제하지 않고 가장 앞 요소를 반환함
    def __init__(self):
        self.front = None
        self.rear = None
        self.queue = []


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
    
    
queue = MyQueue()
queue.enQueue(5)
queue.enQueue(4)
queue.enQueue(3)
queue.enQueue(2)
queue.enQueue(1)

print(queue.deQueue())
print(queue.deQueue())
print(queue.deQueue())
print(queue.deQueue())
print(queue.deQueue())