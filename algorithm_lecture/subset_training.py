# [부분 집합] 민철이는 {A, B, C, D, E}의 친구가 있다. 이 중 최소 2명 이상의 친구를 선정하여 함께 카페를 가려고 한다면, 
# 총 몇 가지의 경우가 가능할까?

friends = {'A', 'B', 'C', 'D', 'E'}
n = len(friends)           # 최소 2명 이상(?)

def get_sub(target):
    cnt = 0                 # 1의 개수를 셀 수 있음
    for i in range(n):
        if target & 0x1:
            # print(friends[i], end = ' ')
            cnt += 1
        target >>= 1
    return cnt


result = 0
for target in range(2, 1 << n):
    if get_sub(target) >= 2:            # bit 2개 이상 1이라면,
        result += 1
print(result)