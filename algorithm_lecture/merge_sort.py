# 1. 분할 과정
def merge_sort(lst):
    if len(lst) == 1:
        return lst
    
    left = []
    right = []

    middle = len(lst) // 2

    for x in lst[:middle]:
        left.append(x)

    for y in lst[middle:]:
        right.append(y)

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


# 2. 병합 과정
def merge(left, right):
    result = []

    while 0 < len(left) or 0 < len(right):
        if 0 < len(left) and 0 < len(right):
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif len(left) > 0:
            result.append(left.pop(0))
        elif len(right) > 0:
            result.append(right.pop(0))

    return result


arr = [69, 10, 30, 2, 16, 8, 31, 22]
arr = merge_sort(arr)
print(arr)
