# 5. 효율적인 화폐 구성 (시간 제한 1초)
# N종류의 화폐가 있을 때, 화폐의 개수를 최소로 하여 그 가치의 합이 M원이 되도록 하려고 한다.

N, M = map(int, input().split())
money = []
for _ in range(N):
    money += [int(input())]
money.sort(reverse=True)

d = [float('inf')] * (M + 1)

for m in money:
    d[m] = 1

for n in range(money[-1], M + 1):
    if d[n] == float('inf'):
        for m in money:
            if n - m >= money[-1] and d[n - m] != float('inf'):
                d[n] = min(d[n], d[n - m] + 1)
                break

if d[M] == float('inf'):
    print(-1)
else:
    print(d[M])
