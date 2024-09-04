# 분할 정복 기법(Divide and Conquer)
def recursive_power(x, n):
    if n == 1:
        return x
    if n % 2 == 0:
        y = recursive_power(x, n/2)
        return y ** 2
    else:
        y = recursive_power(x, (n - 1) / 2)
        return (y ** 2)* x
    

result = recursive_power(2, 3)

print(result)