# from pprint import pprint

# matrix = []
# for _ in range(10):
#     lst = []
#     for __ in range(10):
#         lst.append(0)
#     matrix.append(lst)

# pprint(matrix)


# string = 'abc'
# print(len(string))

lst = [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1]

# idx = lst.index(1)
# print(idx)             # 0
# idx = lst[idx + 1:].index(1)
# print(idx)         # 3

# idx_lst = [-1]

# for _ in range(lst.count(1)):
#     idx = lst[idx_lst[-1] + 1:].index(1)
#     idx_lst.append(idx_lst[-1] + idx + 1)

# idx_lst.pop(1)
# print(idx_lst)

dictionary = {'a':1, 'b':2}

print(list(dictionary.values()))