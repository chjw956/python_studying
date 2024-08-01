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

idx = -1
idx_lst = []

for _ in range(lst.count(1)):
    idx = lst[idx + 1:].index(1)
    if idx_lst != []:
        idx_lst.append(idx_lst[-1] + idx)
    else:
        idx_lst.append(idx)

print(idx_lst)