# [도전] 중복순열 [1, 1, 1] ~ [6, 6, 6]까지 출력하는 코드를 재귀호출로 구현하자.

# 내가 짠 코드
def permutation(empty, num, k, used):
    if len(empty) == k:
        print(empty)
        return empty    

    for n in range(1, num + 1):
        if not used[n]:
            permutation(empty + [n], num, k, used)


num = 6
k = 3
used = [False for _ in range(num + 1)]
permutation([], num, k, used)




# 라이브 강사님이 짜신 코드

def recur(level):
    # 1.기저 조건
    if level == 3:
        print(*path)
        return

    # 2. 후보군을 반복하면서
    for i in range(1, 7):
        # i가 이미 사용됐다면, pass  (이건 굉장히 비효율적인 코드임 -> 중복 제거된 순열 버전)
        # 시간 초과 위험도가 높음 -> 따라서 used를 사용해주는 것이 훨씬 효율적임
        if i in path:
            continue
        # 2-1. 재귀 호출 전 경로 기록
        path.append(i)
        # 2-2. 다음 재귀 호출 (파라미터 전달)
        recur(level + 1)
        # 2-3. 돌아왔을 때 - 사용했던 경로를 삭제함
        path.pop()


# 호출: 시작점을 함께 전달해주는 경우가 많음
recur(0)