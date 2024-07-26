# 99-dict-practice-01

# 각 혈액형의 인원수를 계산하는 딕셔너리를 생성하기.
blood_types = ['A', 'B', 'O', 'AB', 'A', 'O', 'B', 'A', 'AB', 'O', 'A', 'B']


# 1. [] 표기법을 사용한 방법
def count_blood_types(blood_types):
    people_num = dict()
    for type in blood_types:
        if type in people_num:
            people_num[type] += 1
        else:
            people_num[type] = 1

    return people_num


print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}


# 2. get() 메서드를 사용한 방법
def count_blood_types(blood_types):
    people_num = dict()
    
    for b in blood_types:
        people_num[b] = people_num.get(b, 0) + 1

    return people_num

print(count_blood_types(blood_types))  # {'A': 4, 'B': 3, 'O': 3, 'AB': 2}
