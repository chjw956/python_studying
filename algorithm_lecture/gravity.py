"""
배열 활용 예제: Gravity

상자들이 쌓여있는 방이 있다.
방이 오른쪽으로 90도 회전하여 상자들이 중력의 영향을 받아 낙하한다고 할 때, 
낙차가 가장 큰 상자를 구하여 그 낙차를 리턴하는 프로그램을 작성하시오.

-> 각 열의 꼭대기 상자들이 몇 칸 떨어지는지 계산하기 (강사님 방식)

-> 행렬을 만들어서 해결 (내 생각)
"""
from pprint import pprint as print


N = int(input())            
height_list = list(map(int, input().split()))

matrix = []
for h in height_list:
    lst = [1]*h + [0] * (N - h)
    matrix.append(lst)

line = matrix[0]
c_list = []

for l in range(len(line)):
    c = 0
    if line[l] == 1:
        for r in range(1, N):
            if matrix[r][l] == 0:
                c += 1       
        c_list.append(c)

c_list.sort()
print(c_list[-1])

    
