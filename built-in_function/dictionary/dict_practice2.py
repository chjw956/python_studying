# 99-dict-practice-02

# 딕셔너리를 입력받아 value와 key를 뒤집은 결과를 반환하는 함수 `dict_invert()`를 작성하기

# 1. [] 표기법을 사용한 방법
# def dict_invert(input_dict):
#     invert_dict = dict()

#     for k, v in input_dict.items():
#         if v not in invert_dict.keys():
#             invert_dict[v] = [k]
#         else:
#             invert_dict[v].extend([k])

#     return invert_dict


# 2. get() 메서드를 사용한 방법
# def dict_invert(input_dict):
#     invert_dict = dict()

#     for k in input_dict.items():
#         invert_dict[input_dict.get(k)] += [k]

#     return invert_dict


# 3. setdefault 메서드를 사용한 방법
def dict_invert(input_dict):
    invert_dict = dict()

    for k, v in input_dict.items():
        invert_dict.setdefault(v, [])
        invert_dict[v].append(k)
    
    return invert_dict


print(dict_invert({1: 10, 2: 20, 3: 30}))  # {10: [1], 20: [2], 30: [3]}

print(
    dict_invert({1: 10, 2: 20, 3: 30, 4: 30})  # {10: [1], 20: [2], 30: [3, 4]}
)  

print(dict_invert({1: True, 2: True, 3: True}))  # {True: [1, 2, 3]}
