# di = [0, 1, 0, -1]
# dj = [1, 0, -1, 0]

# print(list(zip(di, dj)))


# 비트맵 만들기
N = 5                                   # n : 원소의 개수

# 부분 집합의 개수만큼 반복
for i in range(1 << N):                 # 1 << n : 부분 집합의 개수
    for j in range(N-1, -1, -1):        # 원소의 수만큼 비트를 비교함
        if i & (1 << j):                # i의 j번째 비트가 1이라면
            print(1, end = ", ")        
            # print(arr[j], end=", ")     # j번 원소 출력
        else:
            print(0, end = ", ")
    print()
