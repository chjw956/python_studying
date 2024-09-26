# 5. 효율적인 화폐 구성 (시간 제한 1초)
# N종류의 화폐가 있을 때, 화폐의 개수를 최소로 하여 그 가치의 합이 M원이 되도록 하려고 한다.

N, M = map(int, input().split())
money = list(map(int, input() for _ in range(N)))

