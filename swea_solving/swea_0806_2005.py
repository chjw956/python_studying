# SWEA 2005.파스칼의 삼각형 (D2)
# 스택 사용하기!
# 메모이제이션 사용하기

T = int(input())

for test_case in range(T):
    N = int(input())
    my_stack = []
    top = -1

    for i in range(N):
        if i == 0:
            v = 1
            print(v)
            my_stack.append(1)
            top += 1            
        else:
            for j in range(i):
                v = my_stack[top]
                print(v, end=' ')

                if j + 1 == i:
                    print(1)
                    my_stack.append(1)
                    top += 1
                    break

                v += my_stack[top]
                print(v, end = ' ')
                v =  my_stack.pop()
                top -= 1

                
