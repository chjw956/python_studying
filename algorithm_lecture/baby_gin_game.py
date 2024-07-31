# 완전 검색 알고리즘 접근 방법
"""
예를 들어, 입력으로 [2, 3, 5, 7, 7, 7]을 받은 경우, 아래와 같이 순열 생성 가능하다.

[2, 3, 5, 7, 7, 7]
[2, 3, 7, 5, 7, 7]
...
[7, 7, 7, 5, 3, 2]

위의 순열에 대하여 앞의 3자리와 뒤의 3자리를 잘라, 
run 또는 triplet 여부를 테스트하고 최종적으로 baby-gin을 판단한다.
"""
# 딕셔너리로 만들기?
# 내 방법보다는 정석적인 방법부터 습득하는 게 우선인 것 같은데..


lst = [2, 3, 5, 7, 7, 7]

# 순열 생성
# def make_permutation(lst):
#     used = [0 for _ in range(len(lst))]

#     def generate(chosen, used):
#         if len(chosen) == 


# 재귀를 이용한 순열 구현(ver1)
def permutation(arr, r):
    # 1.
    arr = sorted(arr)
    used = [0 for _ in range(len(arr))]

    def generate(chosen, used):
        # 2.
        if len(chosen) == r:
            print(chosen)
            return
	
	# 3.
        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen, used)
                used[i] = 0
                chosen.pop()
    generate([], used)


# 재귀를 이용한 순열 구현(ver2)
def printPermutation(number, digit):
    permutation[digit] = number
    if(digit == N - 1):
        for i in permutation:
            print(i, end = ' ')
        print()
        return
    for i in range(1, N + 1):
        if visited[i]: 
            continue
        visited[i] = True
        printPermutation(i,digit+1)
        visited[i] = False


N = int(input())

visited = [False for i in range(N + 1)]
print(f'visited = {visited}')

permutation = [0] * N

for i in range(1, N + 1):
    visited[i] = True
    printPermutation(i, 0)
    visited[i] = False


# permutation(lst, 6)





# 탐욕 알고리즘 접근 방법
"""
- 6개의 숫자는 6자리의 정수 값으로 입력됨
- counts 배열의 각 원소를 체크하여 run과 triplet 및 baby-gin 여부를 판단함
"""
"""
num = 456789            # Baby Gin 확인할 6자리 수
c = [0] * 12            # 6자리 수로부터 각 자리 수를 추출하여 개수를 누적할 리스트

for i in range(6):
    c[num % 10] += 1
    num //= 10

i = 0
tri = run = 0

while i < 10:
    # triplet 조사 후 데이터 삭제
    if c[i] >= 3:       
        c[i] -= 3
        tri += 1
        continue
    
    # run 조사 후 데이터 삭제
    if c[i] >= 1 and c[i+1] >= 1 and c[i+2] >= 1 :
        c[i] -= 1
        c[i + 1] -= 1
        c[i + 2] -= 1
        run += 1
        continue
    i += 1

if run + tri == 2 :
    print("Baby Gin")
else:
    print("Lose")
"""