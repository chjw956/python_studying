# 바이너리 카운팅(Binary Counting)

arr = ['A', 'B', 'C']
n = len(arr)

def get_sub(target):
    for i in range(n):
        # 비트 하나하나를 확인하여 1이라면 출력한다.
        if target & 0x1:
            print(arr[i], end = ' ')
        target >>= 1


for target in range(0, 1 << n):            # range(0, 8)
    print('{', end = ' ')
    get_sub(target)
    print('}')