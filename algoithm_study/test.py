N = int(input())

for _ in range(N):
    # tuple이 아니라 generator 객체로 생성됨
    print(tuple((x, y) for x, y in map(int, input().split())))


coordinate = tuple((x, y) for x, y in zip(map(int, input().split()[::2]), map(int, input().split()[1::2])))

input_values = list(map(int, input().split()))

coordinate = tuple((input_values[i], input_values[i+1]) for i in range(0, len(input_values), 2))
