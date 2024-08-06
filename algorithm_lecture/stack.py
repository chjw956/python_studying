# 24.08.06.(화) [Stack] 스택을 구현해보고, 3개의 데이터를 스택에 저장하고 다시 3번 꺼내어 출력해보자.

class MyStack:
    def __init__(self, size):
        self.top = -1
        self.size = size
        self.stack_lst = [0] * size
        
    
    def push(self, e):
        self.top += 1
        if self.top == self.size:
            print('overflow!')
        else:
            self.stack_lst[self.top] = e
            

    def pop(self):
        if self.top == -1:
            print('underflow!')
            return 0
        else:
            self.top -= 1
            return self.stack_lst[self.top + 1]
        

stck = MyStack(10)
stck.push(1)
stck.push(2)
stck.push(3)

print(stck.pop())
print(stck.pop())
print(stck.pop())

