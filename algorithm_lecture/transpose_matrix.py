# transpose matrix(전치 행렬)
arr = [
    '123',
    '456',
    '789'
    ]

arr = list(zip(*arr))

for row in arr:
    print(row)

