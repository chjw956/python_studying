import sys
sys.stdin = open('sample_input(1).txt', 'r')

for test_case in range(10):
    N = int(input())
    heights = list(map(int, input().split()))

    houses = 0

    for idx in range(len(heights)):
        if heights[idx] == 0 :
            continue

        if heights[idx] > heights[idx - 1] and heights[idx] > heights[idx -2] \
            and heights[idx] > heights[idx + 1] and heights[idx] > heights[idx + 2]:
            
            max_v = max(heights[idx - 1], heights[idx - 2], heights[idx + 1], heights[idx + 2])

            min = heights[idx] - max_v
            houses += min
            # print(f'min = {min}, houses = {houses}')
         
    print(f'#{test_case + 1} {houses}')


"""
# 강사님 코드 (코드를 모듈화 해서 짜는 방법을 항상 고려하라고 하심)


# 건물 정보를 인자로 받아 조망권을 가진 세대 수를 반환하는 함수
def solve(buildings):
    
    result = 0          # 조망권을 가진 세대 수를 저장할 변수
    
    # 건물을 2 ~ N - 3까지 반복함
    for i in range(2, N - 2):
        for j in range(i - 2, i + 3):
            if j == i:
                continue
            
                
        pass
    
        
    return result
    



for test_case in range(1, 11):
    N = int(input())

    buildings = list(map(int, input().split()))
    
    result = solve(buildings)

    print(f'#{test_case} {result}')


"""