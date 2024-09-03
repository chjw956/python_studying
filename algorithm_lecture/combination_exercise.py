# 주사위 눈금 N개를 던져서 나올 수 있는 모든 조합을 출력하라. (N = 3)

dice = [1, 2, 3, 4, 5, 6]
N = 3
path = []

def run(lev, start):
    if lev == N:
        print(path)
        return
    
    for i in range(start, len(dice)):
        path.append(dice[i])
        run(lev + 1, i + 1)
        path.pop()


run(0, 0)