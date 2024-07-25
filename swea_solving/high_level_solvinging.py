# 1486. 장훈이의 높은 선반 (D4)
# 재귀함수 적용

import sys
sys.stdin = open("input4_1.txt", "r")

n_list = []
small = 0

def black_box(t, lst):
    global n_list
    global small
    # print(f"t = {t}, lst = {lst}")
    if lst == []:
        return t
    n = lst[0]
    if n <= t:
        lst.pop(0)
        
        print(f"t = {t}, n = {n}, small = {small}, lst = {lst}")
        s1 = black_box(t - n, lst)
        s2 = black_box(t, lst)
        
        print(f"s1 = {s1}, s2 = {s2}", end="\n")
        small = s2

        # small이 제대로 활용이 안되고 있음
        if s1 < s2:
            small = s1
        else:
            n_list.append(n)
        return small

    return t


T = int(input())

for t in range(T):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()
    HS = sum(H)

    target = HS - B
    copy_h = H[:]

    print(f"target = {target}")
    result = black_box(target, copy_h)
    print(f"#{t + 1} {result}, n_list = {n_list}")
    print()










"""
# 이렇게 하면 반환 값에 일관성이 없나..?
def to_small(t, lst):
    print(f'target = {t}')
    if lst == [] or t <= 0:
        return t

    for l in lst:
        if t >= l:
            s1 = to_small(t, lst)
            t -= l
            lst.pop(lst.index(l))
            s2 = to_small(t)
            if 
        else:
            return t
    return t


T = int(input())

for t in range(T):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    # H.sort(reverse=True)
    H.sort()
    copy_h = H[:]
    # H.sort()
    HS = sum(H)

    for h in H:
        target = HS - B
        if target <= h or copy_h == []:
            print(f"#{t+1} {abs(target)}")
            break
        
        target -= h
        copy_h.pop(0)

        result = to_small(target, copy_h)
        print(f"#{t+1} {abs(result)}")
        break


"""




        





"""
# 나의 풀이(였던 것)..

T = int(input())
# T = 1

for t in range(T):
    N, B = map(int, input().split())
    staff_list = list(map(int, input().split()))
    staff_list.sort()

    copy_list = staff_list[:]

    target = B
    count = 0
    
    while len(copy_list) > 0 and target <= B and target > 0:
        print(f"copy_list = {copy_list}")
        difference_list = []
        count += 1
        # 계속 절댓값 작은 것만 찾아 가면 됨(?_? 아닌 것 같은데..)
        if count == 1:
            for i in range(len(copy_list)):
                difference_list.append((i, B - copy_list[i]))
        else:
            for i in range(len(copy_list)):
                difference_list.append((i, target - copy_list[i]))
                # print(f"difference_list = {difference_list}")
        
        # difference_list.sort(key = lambda x:abs(x[1]))
        difference_list.sort(key = lambda x:x[1])

        print(f"difference_list = {difference_list}")

        if len(difference_list) > 1:
            if difference_list[0][1] > 0 and difference_list[1][1] <= 0:
                target -= copy_list[difference_list[1][0]]
                print("here1")
            else:
                target -= copy_list[difference_list[0][0]]
                print("here2")
        else:
            target -= copy_list[difference_list[0][0]]
            print("here3")

        print(f"target = {target}")
        print()
        del copy_list[difference_list[0][0]]
        copy_list.sort()
    
    print(f"#{t+1}", abs(target))
    print()
"""


"""
# 가져온 답안

# a : 현재 달성한 수치
def search(h,b,a,):          # list, sum-B, 0
        if h == []:
            return b-a
        
        HI = h[-1]
        # 어떻게 이런 조건을 생각했는지 이해가 안 감
        if HI > b - a:
            h.pop()
            return search(h,b,a)
        
        else:
            hc = h[:]
            h.pop()
            s1 = search(h,b,a+HI)
            hc.pop()
            s2 = search(hc,b,a)

            if s1 <= s2 :
                return s1
            else:
                return s2

T = int(input())
# T = 1

for test_case in range(1, T + 1):

    N, B = map(int, input().split())
    H = sorted(list(map(int,input().split())))
    SUM = sum(H)

    print(f'#{test_case} {search(H,SUM-B,0)}')

"""


