def binary_search(array, target, start, end):
    result = []
    result.append(start)

    for i in range(end + 1):
        if array[i] > result[-1]:
            result.append(array[i])
        elif array[i]